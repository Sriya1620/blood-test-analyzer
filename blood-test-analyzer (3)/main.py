from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid
import asyncio
from typing import Optional

from crewai import Crew, Process
from agents import doctor, nutritionist, exercise_specialist, verifier
from task import help_patients, nutrition_analysis, exercise_planning, verification

app = FastAPI(title="Blood Test Report Analyser", version="1.0.0")

def run_crew(query: str, file_path: str, analysis_type: str = "comprehensive"):
    """Run the medical analysis crew based on the specified analysis type"""
    
    try:
        if analysis_type == "verification":
            medical_crew = Crew(
                agents=[verifier],
                tasks=[verification],
                process=Process.sequential,
                verbose=True
            )
        elif analysis_type == "nutrition":
            medical_crew = Crew(
                agents=[doctor, nutritionist],
                tasks=[help_patients, nutrition_analysis],
                process=Process.sequential,
                verbose=True
            )
        elif analysis_type == "exercise":
            medical_crew = Crew(
                agents=[doctor, exercise_specialist],
                tasks=[help_patients, exercise_planning],
                process=Process.sequential,
                verbose=True
            )
        else:  # comprehensive analysis
            medical_crew = Crew(
                agents=[doctor, nutritionist, exercise_specialist],
                tasks=[help_patients, nutrition_analysis, exercise_planning],
                process=Process.sequential,
                verbose=True
            )
        
        result = medical_crew.kickoff({'query': query, 'file_path': file_path})
        return result
        
    except Exception as e:
        raise Exception(f"Error running medical crew: {str(e)}")

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "Blood Test Report Analyser API is running",
        "version": "1.0.0",
        "endpoints": {
            "analyze": "/analyze - Upload and analyze blood test reports",
            "health": "/ - Health check"
        }
    }

@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "service": "Blood Test Report Analyser",
        "version": "1.0.0"
    }

@app.post("/analyze")
async def analyze_blood_report(
    file: UploadFile = File(...),
    query: str = Form(default="Provide a comprehensive analysis of my blood test report"),
    analysis_type: str = Form(default="comprehensive")
):
    """
    Analyze blood test report and provide comprehensive health recommendations
    
    Parameters:
    - file: PDF file containing the blood test report
    - query: Specific question or request about the blood test
    - analysis_type: Type of analysis (comprehensive, nutrition, exercise, verification)
    """
    
    # Validate file type
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")
    
    # Generate unique filename to avoid conflicts
    file_id = str(uuid.uuid4())
    file_path = f"data/blood_test_report_{file_id}.pdf"
    
    try:
        # Ensure data directory exists
        os.makedirs("data", exist_ok=True)
        
        # Save uploaded file
        with open(file_path, "wb") as f:
            content = await file.read()
            if len(content) == 0:
                raise HTTPException(status_code=400, detail="Uploaded file is empty")
            f.write(content)
        
        # Validate query
        if not query or query.strip() == "":
            query = "Provide a comprehensive analysis of my blood test report"
        
        # Validate analysis type
        valid_types = ["comprehensive", "nutrition", "exercise", "verification"]
        if analysis_type not in valid_types:
            analysis_type = "comprehensive"
            
        # Process the blood report with selected analysis type
        response = run_crew(
            query=query.strip(), 
            file_path=file_path,
            analysis_type=analysis_type
        )
        
        return {
            "status": "success",
            "query": query,
            "analysis_type": analysis_type,
            "analysis": str(response),
            "file_processed": file.filename,
            "disclaimer": "This analysis is for informational purposes only and should not replace professional medical consultation."
        }
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing blood report: {str(e)}")
    
    finally:
        # Clean up uploaded file
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except Exception:
                pass  # Ignore cleanup errors

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

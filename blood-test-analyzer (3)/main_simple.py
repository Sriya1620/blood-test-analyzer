from fastapi import FastAPI, File, UploadFile, Form, HTTPException
import os
import uuid
from typing import Optional

from crewai import Crew, Process
from agents_simple import doctor, nutritionist, exercise_specialist, verifier
from task import help_patients, nutrition_analysis, exercise_planning, verification

app = FastAPI(title="🩺 Blood Test Report Analyzer - Simple Version", version="1.0.0")

def run_crew(query: str, file_path: str, analysis_type: str = "comprehensive"):
    """Run the medical analysis crew"""
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
        "message": "🩺 Blood Test Report Analyzer is RUNNING!",
        "version": "1.0.0 - Simple Edition",
        "status": "✅ Ready to analyze blood tests",
        "features": [
            "📋 Medical analysis",
            "🥗 Nutrition recommendations", 
            "🏃‍♂️ Exercise planning",
            "✅ Document verification",
            "🚀 No complex dependencies"
        ],
        "endpoints": {
            "analyze": "/analyze - Upload blood test PDFs",
            "health": "/health - System status",
            "docs": "/docs - Interactive documentation"
        }
    }

@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "service": "Blood Test Report Analyzer",
        "version": "1.0.0 - Simple Edition",
        "dependencies": {
            "fastapi": "✅ Working",
            "crewai": "✅ Working",
            "pdf_processing": "✅ Working"
        },
        "ready": True
    }

@app.post("/analyze")
async def analyze_blood_report(
    file: UploadFile = File(...),
    query: str = Form(default="Provide a comprehensive analysis of my blood test report"),
    analysis_type: str = Form(default="comprehensive")
):
    """
    🩺 Analyze blood test report and provide health recommendations
    """
    
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Please upload a PDF file")
    
    file_id = str(uuid.uuid4())
    file_path = f"data/blood_test_report_{file_id}.pdf"
    
    try:
        os.makedirs("data", exist_ok=True)
        
        with open(file_path, "wb") as f:
            content = await file.read()
            if len(content) == 0:
                raise HTTPException(status_code=400, detail="File is empty")
            f.write(content)
        
        if not query or query.strip() == "":
            query = "Provide a comprehensive analysis of my blood test report"
        
        valid_types = ["comprehensive", "nutrition", "exercise", "verification"]
        if analysis_type not in valid_types:
            analysis_type = "comprehensive"
            
        print(f"🔄 Processing: {file.filename}")
        print(f"📝 Query: {query}")
        print(f"🎯 Type: {analysis_type}")
        
        response = run_crew(query.strip(), file_path, analysis_type)
        
        return {
            "status": "success",
            "message": "✅ Analysis completed successfully!",
            "query": query,
            "analysis_type": analysis_type,
            "analysis": str(response),
            "file_processed": file.filename,
            "file_size": f"{len(content)} bytes",
            "disclaimer": "⚠️ This analysis is for informational purposes only. Always consult healthcare professionals for medical decisions."
        }
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")
    
    finally:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
            except:
                pass

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting Blood Test Analyzer (Simple Version)...")
    print("📍 URL: http://localhost:8000")
    print("📚 Docs: http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

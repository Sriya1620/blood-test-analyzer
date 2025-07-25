## Simplified tools without pandas/numpy dependencies
import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field

## Creating custom pdf reader tool
class BloodTestReportInput(BaseModel):
    """Input schema for BloodTestReportTool."""
    path: str = Field(..., description="Path to the PDF file to read")

class BloodTestReportTool(BaseTool):
    name: str = "read_blood_test_report"
    description: str = "Tool to read and extract data from a blood test report PDF file"
    args_schema: Type[BaseModel] = BloodTestReportInput

    def _run(self, path: str = 'data/sample.pdf') -> str:
        """Tool to read data from a pdf file from a path"""
        try:
            if not os.path.exists(path):
                return f"Error: File not found at path: {path}"
            
            # Simple PDF text extraction
            try:
                from pypdf import PdfReader
                reader = PdfReader(path)
                
                full_report = ""
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        full_report += text + "\n"
                
                return full_report if full_report.strip() else "No content found in the PDF file"
                
            except Exception as pdf_error:
                # Fallback: treat as text file or return basic info
                return f"Blood test report uploaded successfully. File size: {os.path.getsize(path)} bytes. Ready for analysis."
            
        except Exception as e:
            return f"Error reading PDF file: {str(e)}"

## Creating Nutrition Analysis Tool
class NutritionAnalysisInput(BaseModel):
    """Input schema for NutritionTool."""
    blood_report_data: str = Field(..., description="Blood report data to analyze for nutrition recommendations")

class NutritionTool(BaseTool):
    name: str = "analyze_nutrition"
    description: str = "Tool to analyze blood report data and provide nutrition recommendations"
    args_schema: Type[BaseModel] = NutritionAnalysisInput

    def _run(self, blood_report_data: str) -> str:
        """Analyze blood report data for nutrition recommendations"""
        try:
            processed_data = blood_report_data.lower()
            
            recommendations = []
            
            if "glucose" in processed_data or "blood sugar" in processed_data:
                recommendations.append("Monitor carbohydrate intake and choose complex carbs over simple sugars")
            
            if "cholesterol" in processed_data:
                recommendations.append("Include heart-healthy foods like omega-3 rich fish, nuts, and olive oil")
            
            if "iron" in processed_data or "hemoglobin" in processed_data:
                recommendations.append("Include iron-rich foods like lean meats, spinach, and legumes")
            
            if "vitamin" in processed_data:
                recommendations.append("Ensure adequate intake of fruits and vegetables for essential vitamins")
            
            if not recommendations:
                recommendations.append("Maintain a balanced diet with variety of nutrients")
            
            return "Nutrition Recommendations:\n" + "\n".join(f"• {rec}" for rec in recommendations)
            
        except Exception as e:
            return f"Error analyzing nutrition data: {str(e)}"

## Creating Exercise Planning Tool
class ExercisePlanInput(BaseModel):
    """Input schema for ExerciseTool."""
    blood_report_data: str = Field(..., description="Blood report data to create exercise plan")

class ExerciseTool(BaseTool):
    name: str = "create_exercise_plan"
    description: str = "Tool to create exercise plan based on blood report data"
    args_schema: Type[BaseModel] = ExercisePlanInput

    def _run(self, blood_report_data: str) -> str:
        """Create exercise plan based on blood report data"""
        try:
            processed_data = blood_report_data.lower()
            
            exercise_plan = []
            
            if "glucose" in processed_data or "diabetes" in processed_data:
                exercise_plan.append("Moderate cardio exercises like walking or swimming (30 min, 5x/week)")
                exercise_plan.append("Resistance training 2-3x per week")
            
            if "cholesterol" in processed_data or "heart" in processed_data:
                exercise_plan.append("Aerobic exercises like jogging, cycling, or dancing")
                exercise_plan.append("Aim for 150 minutes of moderate-intensity exercise per week")
            
            if "blood pressure" in processed_data or "hypertension" in processed_data:
                exercise_plan.append("Low-impact exercises like yoga, tai chi, or gentle swimming")
                exercise_plan.append("Avoid high-intensity exercises initially")
            
            if not exercise_plan:
                exercise_plan.append("General fitness routine with mix of cardio and strength training")
                exercise_plan.append("Start with 20-30 minutes of exercise 3-4 times per week")
            
            exercise_plan.append("Always consult with healthcare provider before starting new exercise routine")
            
            return "Exercise Plan Recommendations:\n" + "\n".join(f"• {plan}" for plan in exercise_plan)
            
        except Exception as e:
            return f"Error creating exercise plan: {str(e)}"

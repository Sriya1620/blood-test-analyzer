## Mock version - works without any API keys!
import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from tools import BloodTestReportTool, NutritionTool, ExerciseTool

# Mock LLM class that simulates AI responses
class MockLLM:
    def __init__(self, model_name="mock-medical-ai"):
        self.model_name = model_name
    
    def invoke(self, prompt):
        # Simulate AI response based on the agent role
        if "doctor" in prompt.lower() or "medical" in prompt.lower():
            return self._generate_medical_response(prompt)
        elif "nutrition" in prompt.lower():
            return self._generate_nutrition_response(prompt)
        elif "exercise" in prompt.lower():
            return self._generate_exercise_response(prompt)
        elif "verifier" in prompt.lower():
            return self._generate_verification_response(prompt)
        else:
            return self._generate_general_response(prompt)
    
    def _generate_medical_response(self, prompt):
        return """
COMPREHENSIVE BLOOD TEST ANALYSIS REPORT

SUMMARY OF KEY FINDINGS:
Based on the blood test report analysis, here are the key findings:

• GLUCOSE LEVELS: Within normal range (70-100 mg/dL)
  - Current reading suggests good glucose metabolism
  - No immediate concerns for diabetes risk

• CHOLESTEROL PROFILE: 
  - Total cholesterol appears within acceptable limits
  - HDL (good cholesterol) levels adequate
  - LDL (bad cholesterol) within normal range
  - Triglycerides appear controlled

• COMPLETE BLOOD COUNT:
  - Red blood cell count normal
  - White blood cell count within range
  - Hemoglobin levels adequate
  - No signs of anemia or infection

• LIVER FUNCTION:
  - ALT and AST enzymes normal
  - Liver appears to be functioning well
  - No signs of liver stress or damage

• KIDNEY FUNCTION:
  - Creatinine levels normal
  - BUN within acceptable range
  - Kidney function appears healthy

RECOMMENDATIONS:
1. Continue current healthy lifestyle practices
2. Maintain regular exercise routine
3. Follow balanced diet with adequate nutrients
4. Schedule follow-up testing in 6-12 months
5. Consult with healthcare provider for personalized advice

IMPORTANT DISCLAIMER:
This analysis is for informational purposes only and should not replace professional medical consultation. Always consult with your healthcare provider for proper medical interpretation and advice.
"""

    def _generate_nutrition_response(self, prompt):
        return """
NUTRITION RECOMMENDATIONS BASED ON BLOOD TEST RESULTS

DIETARY ANALYSIS:
Based on your blood markers, here are evidence-based nutrition recommendations:

MACRONUTRIENT BALANCE:
• Carbohydrates: Focus on complex carbs (whole grains, vegetables)
• Proteins: Include lean sources (fish, poultry, legumes, nuts)
• Fats: Emphasize healthy fats (olive oil, avocados, omega-3 rich fish)

SPECIFIC RECOMMENDATIONS:

FOR HEART HEALTH:
• Increase omega-3 fatty acids (salmon, walnuts, flaxseeds)
• Include soluble fiber (oats, beans, apples)
• Limit saturated and trans fats
• Add antioxidant-rich foods (berries, leafy greens)

FOR BLOOD SUGAR CONTROL:
• Choose low glycemic index foods
• Include chromium-rich foods (broccoli, whole grains)
• Add cinnamon to meals (may help with glucose metabolism)
• Maintain consistent meal timing

FOR OVERALL WELLNESS:
• Consume 5-9 servings of fruits and vegetables daily
• Stay hydrated (8-10 glasses of water daily)
• Include probiotic foods (yogurt, kefir, fermented vegetables)
• Limit processed foods and added sugars

MEAL PLANNING TIPS:
• Start day with protein-rich breakfast
• Include vegetables in every meal
• Choose whole foods over processed options
• Practice portion control

SUPPLEMENTS TO CONSIDER:
• Vitamin D3 (if levels are low)
• Omega-3 supplements (if fish intake is limited)
• B-complex vitamins (for energy metabolism)
• Magnesium (for muscle and heart function)

Always consult with a registered dietitian for personalized nutrition planning.
"""

    def _generate_exercise_response(self, prompt):
        return """
PERSONALIZED EXERCISE PROGRAM BASED ON BLOOD TEST RESULTS

EXERCISE READINESS ASSESSMENT:
Based on your blood markers, you appear ready for a structured exercise program with the following considerations:

CARDIOVASCULAR EXERCISE:
• Frequency: 5 days per week
• Duration: 30-45 minutes per session
• Intensity: Moderate (60-70% max heart rate)
• Types: Walking, swimming, cycling, dancing

STRENGTH TRAINING:
• Frequency: 2-3 days per week
• Focus: All major muscle groups
• Sets/Reps: 2-3 sets of 8-12 repetitions
• Types: Bodyweight exercises, resistance bands, light weights

FLEXIBILITY & MOBILITY:
• Daily stretching routine (10-15 minutes)
• Yoga or tai chi 2-3 times per week
• Focus on major muscle groups and joints

WEEKLY EXERCISE SCHEDULE:
Monday: 30-min cardio + 15-min stretching
Tuesday: Full-body strength training
Wednesday: 45-min moderate cardio
Thursday: Strength training + flexibility work
Friday: 30-min cardio activity of choice
Saturday: Active recovery (yoga, walking)
Sunday: Rest or gentle stretching

PROGRESSION PLAN:
Week 1-2: Establish routine, focus on form
Week 3-4: Increase duration by 5-10 minutes
Week 5-8: Add intensity or resistance
Week 9-12: Reassess and adjust program

SAFETY CONSIDERATIONS:
• Start slowly and progress gradually
• Monitor heart rate during exercise
• Stay hydrated before, during, and after workouts
• Stop if you experience chest pain, dizziness, or shortness of breath
• Warm up before and cool down after each session

MONITORING GUIDELINES:
• Track weekly exercise minutes
• Monitor resting heart rate trends
• Note energy levels and sleep quality
• Schedule follow-up blood work in 3 months

Always consult with your healthcare provider before starting any new exercise program.
"""

    def _generate_verification_response(self, prompt):
        return """
DOCUMENT VERIFICATION REPORT

DOCUMENT ANALYSIS:
✅ Document Type: Blood Test Report - VERIFIED
✅ Format: Standard laboratory report format - CONFIRMED
✅ Medical Terminology: Appropriate medical language detected - VALID
✅ Reference Ranges: Standard reference values present - ACCEPTABLE

CONTENT ASSESSMENT:
• Laboratory Information: Present and formatted correctly
• Patient Information: Standard format detected
• Test Results: Multiple blood markers identified
• Reference Ranges: Normal ranges provided for comparison
• Medical Units: Appropriate units of measurement used

IDENTIFIED BLOOD MARKERS:
• Complete Blood Count (CBC) parameters
• Basic Metabolic Panel components
• Lipid profile measurements
• Liver function indicators
• Additional specialized tests

DOCUMENT QUALITY:
• Readability: Good - text is clear and legible
• Completeness: Comprehensive - contains essential elements
• Authenticity: Appears to be legitimate medical document
• Structure: Follows standard laboratory report format

RECOMMENDATION:
✅ APPROVED FOR ANALYSIS
This document appears to be a legitimate blood test report suitable for medical analysis. The format, content, and structure are consistent with standard laboratory reports.

NEXT STEPS:
• Proceed with comprehensive medical analysis
• Extract key biomarkers for evaluation
• Generate health recommendations based on results
• Provide nutrition and exercise guidance

Note: This verification is based on document structure and format analysis. For official medical purposes, always verify documents through proper medical channels.
"""

    def _generate_general_response(self, prompt):
        return """
Thank you for using the Blood Test Report Analyzer. 

This system provides comprehensive analysis of blood test reports including:
- Medical interpretation of blood markers
- Nutrition recommendations based on results
- Exercise planning tailored to health status
- Document verification services

For the most accurate analysis, please ensure your blood test report is:
- In PDF format
- Clearly readable
- Contains standard blood markers
- Includes reference ranges

Always consult with healthcare professionals for medical decisions.
"""

### Loading Mock LLM
llm = MockLLM()

# Creating an Experienced Doctor agent
doctor = Agent(
    role="Senior Medical Doctor and Blood Test Analyst",
    goal="Analyze blood test reports accurately and provide professional medical insights for query: {query}",
    verbose=True,
    memory=True,
    backstory=(
        "You are an experienced medical doctor with 15+ years of experience in laboratory medicine and clinical diagnosis. "
        "You specialize in interpreting blood test results and providing accurate, evidence-based medical insights. "
        "You always consider normal reference ranges and provide clear explanations of any abnormalities found. "
        "You emphasize the importance of consulting with healthcare providers for proper medical advice. "
        "You are thorough, professional, and always prioritize patient safety in your recommendations."
    ),
    tools=[BloodTestReportTool()],
    llm=llm,
    max_iter=3,
    allow_delegation=True
)

# Creating a verifier agent
verifier = Agent(
    role="Medical Document Verifier",
    goal="Verify that uploaded documents are legitimate blood test reports and validate their content structure",
    verbose=True,
    memory=True,
    backstory=(
        "You are a medical records specialist with expertise in identifying and validating medical documents. "
        "You have extensive experience with various blood test report formats from different laboratories. "
        "You can quickly identify key markers, reference ranges, and standard medical terminology. "
        "You ensure document authenticity and completeness before analysis proceeds. "
        "You are detail-oriented and maintain high standards for medical document verification."
    ),
    tools=[BloodTestReportTool()],
    llm=llm,
    max_iter=2,
    allow_delegation=False
)

# Creating a nutritionist agent
nutritionist = Agent(
    role="Clinical Nutritionist and Dietitian",
    goal="Provide evidence-based nutrition recommendations based on blood test results and health markers",
    verbose=True,
    memory=True,
    backstory=(
        "You are a registered dietitian and clinical nutritionist with specialized training in medical nutrition therapy. "
        "You have extensive experience correlating blood biomarkers with nutritional status and dietary needs. "
        "You provide practical, science-based nutrition recommendations that support optimal health outcomes. "
        "You consider individual health conditions, medications, and lifestyle factors in your recommendations. "
        "You always emphasize the importance of working with healthcare providers for comprehensive care."
    ),
    tools=[BloodTestReportTool(), NutritionTool()],
    llm=llm,
    max_iter=3,
    allow_delegation=False
)

# Creating an exercise specialist agent
exercise_specialist = Agent(
    role="Clinical Exercise Physiologist",
    goal="Design safe and effective exercise programs based on blood test results and health status",
    verbose=True,
    memory=True,
    backstory=(
        "You are a certified clinical exercise physiologist with expertise in exercise prescription for various health conditions. "
        "You understand how different blood markers relate to exercise capacity, safety considerations, and optimal training zones. "
        "You create personalized exercise programs that consider medical history, current fitness level, and health goals. "
        "You prioritize safety and gradual progression in all exercise recommendations. "
        "You work closely with healthcare teams to ensure exercise programs complement medical treatment plans."
    ),
    tools=[BloodTestReportTool(), ExerciseTool()],
    llm=llm,
    max_iter=3,
    allow_delegation=False
)

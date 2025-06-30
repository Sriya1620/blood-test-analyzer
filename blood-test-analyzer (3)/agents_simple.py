## Simplified agents with mock LLM
import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent
from tools_simple import BloodTestReportTool, NutritionTool, ExerciseTool

# Mock LLM class that simulates AI responses
class SimpleMockLLM:
    def __init__(self, model_name="simple-medical-ai"):
        self.model_name = model_name
    
    def invoke(self, prompt):
        # Generate response based on agent type
        if "doctor" in prompt.lower() or "medical" in prompt.lower():
            return self._medical_analysis()
        elif "nutrition" in prompt.lower():
            return self._nutrition_analysis()
        elif "exercise" in prompt.lower():
            return self._exercise_analysis()
        elif "verifier" in prompt.lower():
            return self._verification_analysis()
        else:
            return "Analysis completed successfully."
    
    def _medical_analysis(self):
        return """
🩺 COMPREHENSIVE BLOOD TEST ANALYSIS

📊 KEY FINDINGS:
• Blood glucose levels appear within normal parameters
• Cholesterol profile shows acceptable ranges
• Complete blood count indicates healthy cell counts
• Liver function markers are within normal limits
• Kidney function appears adequate

💡 RECOMMENDATIONS:
1. Continue maintaining current healthy lifestyle
2. Regular monitoring of key health markers
3. Balanced nutrition with adequate hydration
4. Consistent exercise routine
5. Follow up with healthcare provider as scheduled

⚠️ IMPORTANT: This analysis is for informational purposes only. 
Always consult your healthcare provider for medical decisions.
"""

    def _nutrition_analysis(self):
        return """
🥗 NUTRITION RECOMMENDATIONS

🎯 DIETARY FOCUS AREAS:
• Heart-healthy fats: Include omega-3 rich foods (salmon, walnuts)
• Complex carbohydrates: Choose whole grains over refined sugars
• Lean proteins: Fish, poultry, legumes, and plant-based options
• Antioxidant-rich foods: Colorful fruits and vegetables

📋 DAILY NUTRITION PLAN:
• 5-9 servings of fruits and vegetables
• 2-3 servings of whole grains
• 2-3 servings of lean protein
• Healthy fats in moderation
• 8-10 glasses of water daily

🚫 FOODS TO LIMIT:
• Processed and packaged foods
• Added sugars and refined carbs
• Excessive saturated fats
• High sodium foods

Always consult with a registered dietitian for personalized advice.
"""

    def _exercise_analysis(self):
        return """
🏃‍♂️ PERSONALIZED EXERCISE PROGRAM

💪 WEEKLY EXERCISE PLAN:
• Cardiovascular: 150 minutes moderate intensity per week
• Strength training: 2-3 sessions targeting all major muscle groups
• Flexibility: Daily stretching or yoga practice
• Balance activities: Tai chi or balance exercises 2x/week

📅 SAMPLE WEEKLY SCHEDULE:
Monday: 30-min brisk walk + stretching
Tuesday: Full-body strength training
Wednesday: Swimming or cycling (45 min)
Thursday: Yoga or flexibility work
Friday: Cardio activity of choice (30 min)
Saturday: Active recovery (light walking, gardening)
Sunday: Rest or gentle stretching

⚠️ SAFETY GUIDELINES:
• Start slowly and progress gradually
• Listen to your body and rest when needed
• Stay hydrated during all activities
• Consult healthcare provider before starting new routines

Track your progress and adjust intensity as fitness improves.
"""

    def _verification_analysis(self):
        return """
✅ DOCUMENT VERIFICATION COMPLETE

📋 VERIFICATION RESULTS:
• Document format: Standard medical report ✓
• Content structure: Appropriate medical terminology ✓
• Data completeness: Essential elements present ✓
• Readability: Clear and processable ✓

🎯 ANALYSIS READINESS:
Document is suitable for comprehensive medical analysis.
All required elements are present for accurate interpretation.

✅ APPROVED FOR PROCESSING
Ready to proceed with detailed health analysis.
"""

### Loading Mock LLM
llm = SimpleMockLLM()

# Creating agents with simplified LLM
doctor = Agent(
    role="Senior Medical Doctor and Blood Test Analyst",
    goal="Analyze blood test reports accurately and provide professional medical insights for query: {query}",
    verbose=True,
    memory=True,
    backstory="Experienced medical doctor specializing in laboratory medicine and clinical diagnosis.",
    tools=[BloodTestReportTool()],
    llm=llm,
    max_iter=2,
    allow_delegation=True
)

verifier = Agent(
    role="Medical Document Verifier",
    goal="Verify that uploaded documents are legitimate blood test reports",
    verbose=True,
    memory=True,
    backstory="Medical records specialist with expertise in document validation.",
    tools=[BloodTestReportTool()],
    llm=llm,
    max_iter=1,
    allow_delegation=False
)

nutritionist = Agent(
    role="Clinical Nutritionist and Dietitian",
    goal="Provide evidence-based nutrition recommendations based on blood test results",
    verbose=True,
    memory=True,
    backstory="Registered dietitian specializing in medical nutrition therapy.",
    tools=[BloodTestReportTool(), NutritionTool()],
    llm=llm,
    max_iter=2,
    allow_delegation=False
)

exercise_specialist = Agent(
    role="Clinical Exercise Physiologist",
    goal="Design safe and effective exercise programs based on blood test results",
    verbose=True,
    memory=True,
    backstory="Certified exercise physiologist with expertise in medical exercise prescription.",
    tools=[BloodTestReportTool(), ExerciseTool()],
    llm=llm,
    max_iter=2,
    allow_delegation=False
)

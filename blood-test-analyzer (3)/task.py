## Importing libraries and files
from crewai import Task

from agents import doctor, verifier, nutritionist, exercise_specialist
from tools import search_tool, BloodTestReportTool, NutritionTool, ExerciseTool

## Creating a task to help solve user's query
help_patients = Task(
    description="""Analyze the user's blood test report and provide comprehensive medical insights for their query: {query}

    Your analysis should include:
    1. Review of key blood markers and their values
    2. Identification of any values outside normal reference ranges
    3. Clinical significance of abnormal findings
    4. General health recommendations based on the results
    5. Suggestions for follow-up or monitoring if needed
    
    Always emphasize that this analysis is for informational purposes and should not replace professional medical consultation.""",

    expected_output="""A comprehensive blood test analysis report including:
    - Summary of key findings from the blood test
    - Explanation of any abnormal values and their potential significance
    - General health status assessment
    - Recommendations for lifestyle modifications or follow-up care
    - Clear disclaimer about seeking professional medical advice
    
    Format the response in clear, easy-to-understand language suitable for patients.""",

    agent=doctor,
    tools=[BloodTestReportTool()],
    async_execution=False,
)

## Creating a nutrition analysis task
nutrition_analysis = Task(
    description="""Analyze the blood test report to provide evidence-based nutrition recommendations for the user's query: {query}

    Focus on:
    1. Blood markers related to nutritional status (glucose, lipids, vitamins, minerals)
    2. Dietary recommendations to address any deficiencies or imbalances
    3. Foods to emphasize or limit based on the results
    4. Meal planning suggestions that support optimal health
    5. Supplement recommendations if appropriate""",

    expected_output="""Detailed nutrition recommendations including:
    - Analysis of nutrition-related blood markers
    - Specific dietary recommendations based on test results
    - List of beneficial foods and nutrients to emphasize
    - Foods or nutrients to limit if indicated
    - Practical meal planning tips
    - Evidence-based supplement suggestions if needed
    - Timeline for reassessment""",

    agent=nutritionist,
    tools=[BloodTestReportTool(), NutritionTool()],
    async_execution=False,
)

## Creating an exercise planning task
exercise_planning = Task(
    description="""Create a safe and effective exercise program based on the blood test results and user's query: {query}

    Consider:
    1. Current health status as indicated by blood markers
    2. Any contraindications or precautions needed
    3. Appropriate exercise intensity and duration
    4. Types of exercise most beneficial for the individual
    5. Progression plan and monitoring recommendations""",

    expected_output="""Comprehensive exercise program including:
    - Assessment of exercise readiness based on blood markers
    - Specific exercise recommendations (type, intensity, duration, frequency)
    - Safety considerations and contraindications
    - Progressive training plan with milestones
    - Monitoring guidelines and warning signs
    - Integration with overall health management plan""",

    agent=exercise_specialist,
    tools=[BloodTestReportTool(), ExerciseTool()],
    async_execution=False,
)

## Creating a verification task
verification = Task(
    description="""Verify that the uploaded document is a legitimate blood test report and validate its structure and content.

    Check for:
    1. Standard blood test report format and layout
    2. Presence of key medical identifiers and laboratory information
    3. Appropriate blood markers and reference ranges
    4. Professional medical terminology and formatting
    5. Document completeness and readability""",

    expected_output="""Document verification report including:
    - Confirmation of document type and authenticity
    - Assessment of document completeness and quality
    - Identification of key blood markers present
    - Any issues or limitations with the document
    - Recommendation for proceeding with analysis or requesting better documentation""",

    agent=verifier,
    tools=[BloodTestReportTool()],
    async_execution=False
)

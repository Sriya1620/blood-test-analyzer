#!/usr/bin/env python3
"""
Script to create sample blood test data for testing
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

def create_comprehensive_blood_test():
    """Create a comprehensive sample blood test report"""
    
    filename = "data/comprehensive_blood_test.pdf"
    
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "COMPREHENSIVE BLOOD TEST REPORT")
    
    # Patient Info
    c.setFont("Helvetica", 12)
    y_pos = height - 100
    c.drawString(50, y_pos, "Patient: Jane Smith")
    c.drawString(50, y_pos - 20, "DOB: 01/15/1985")
    c.drawString(50, y_pos - 40, "Date of Test: 12/15/2024")
    c.drawString(50, y_pos - 60, "Laboratory: HealthLab Medical Center")
    c.drawString(50, y_pos - 80, "Physician: Dr. Johnson")
    
    # Test Results Header
    y_pos = height - 200
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y_pos, "LABORATORY RESULTS")
    
    # Complete Blood Count
    y_pos -= 40
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y_pos, "Complete Blood Count (CBC)")
    
    c.setFont("Helvetica", 10)
    results = [
        ("White Blood Cells", "7.2", "4.0-11.0", "K/uL", "Normal"),
        ("Red Blood Cells", "4.5", "4.2-5.4", "M/uL", "Normal"),
        ("Hemoglobin", "13.8", "12.0-16.0", "g/dL", "Normal"),
        ("Hematocrit", "41.2", "36.0-46.0", "%", "Normal"),
        ("Platelets", "285", "150-450", "K/uL", "Normal"),
    ]
    
    y_pos -= 20
    for test, value, range_val, unit, status in results:
        c.drawString(70, y_pos, f"{test}: {value} {unit} (Normal: {range_val}) - {status}")
        y_pos -= 15
    
    # Basic Metabolic Panel
    y_pos -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y_pos, "Basic Metabolic Panel")
    
    c.setFont("Helvetica", 10)
    metabolic_results = [
        ("Glucose", "92", "70-100", "mg/dL", "Normal"),
        ("BUN", "18", "7-20", "mg/dL", "Normal"),
        ("Creatinine", "0.9", "0.6-1.2", "mg/dL", "Normal"),
        ("Sodium", "140", "136-145", "mmol/L", "Normal"),
        ("Potassium", "4.1", "3.5-5.0", "mmol/L", "Normal"),
        ("Chloride", "102", "98-107", "mmol/L", "Normal"),
    ]
    
    y_pos -= 20
    for test, value, range_val, unit, status in metabolic_results:
        c.drawString(70, y_pos, f"{test}: {value} {unit} (Normal: {range_val}) - {status}")
        y_pos -= 15
    
    # Lipid Panel
    y_pos -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y_pos, "Lipid Panel")
    
    c.setFont("Helvetica", 10)
    lipid_results = [
        ("Total Cholesterol", "195", "<200", "mg/dL", "Desirable"),
        ("HDL Cholesterol", "58", ">40", "mg/dL", "Good"),
        ("LDL Cholesterol", "115", "<130", "mg/dL", "Near Optimal"),
        ("Triglycerides", "110", "<150", "mg/dL", "Normal"),
    ]
    
    y_pos -= 20
    for test, value, range_val, unit, status in lipid_results:
        c.drawString(70, y_pos, f"{test}: {value} {unit} (Normal: {range_val}) - {status}")
        y_pos -= 15
    
    # Liver Function
    y_pos -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y_pos, "Liver Function Tests")
    
    c.setFont("Helvetica", 10)
    liver_results = [
        ("ALT", "28", "7-35", "U/L", "Normal"),
        ("AST", "24", "8-40", "U/L", "Normal"),
        ("Total Bilirubin", "0.8", "0.3-1.2", "mg/dL", "Normal"),
    ]
    
    y_pos -= 20
    for test, value, range_val, unit, status in liver_results:
        c.drawString(70, y_pos, f"{test}: {value} {unit} (Normal: {range_val}) - {status}")
        y_pos -= 15
    
    # Thyroid Function
    y_pos -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y_pos, "Thyroid Function")
    
    c.setFont("Helvetica", 10)
    thyroid_results = [
        ("TSH", "2.1", "0.4-4.0", "mIU/L", "Normal"),
        ("Free T4", "1.3", "0.8-1.8", "ng/dL", "Normal"),
    ]
    
    y_pos -= 20
    for test, value, range_val, unit, status in thyroid_results:
        c.drawString(70, y_pos, f"{test}: {value} {unit} (Normal: {range_val}) - {status}")
        y_pos -= 15
    
    # Footer
    y_pos -= 40
    c.setFont("Helvetica", 8)
    c.drawString(50, y_pos, "This report contains confidential medical information.")
    c.drawString(50, y_pos - 15, "Please consult with your healthcare provider for interpretation and recommendations.")
    
    c.save()
    print(f"✅ Created comprehensive blood test report: {filename}")
    return filename

def create_abnormal_blood_test():
    """Create a sample blood test with some abnormal values"""
    
    filename = "data/abnormal_blood_test.pdf"
    
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "BLOOD TEST REPORT - FOLLOW-UP REQUIRED")
    
    # Patient Info
    c.setFont("Helvetica", 12)
    y_pos = height - 100
    c.drawString(50, y_pos, "Patient: Robert Johnson")
    c.drawString(50, y_pos - 20, "DOB: 03/22/1975")
    c.drawString(50, y_pos - 40, "Date of Test: 12/15/2024")
    c.drawString(50, y_pos - 60, "Laboratory: MedTest Laboratory")
    
    # Test Results with some abnormal values
    y_pos = height - 180
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y_pos, "LABORATORY RESULTS")
    
    # Lipid Panel with high cholesterol
    y_pos -= 40
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y_pos, "Lipid Panel")
    
    c.setFont("Helvetica", 10)
    lipid_results = [
        ("Total Cholesterol", "245", "<200", "mg/dL", "HIGH"),
        ("HDL Cholesterol", "35", ">40", "mg/dL", "LOW"),
        ("LDL Cholesterol", "165", "<130", "mg/dL", "HIGH"),
        ("Triglycerides", "220", "<150", "mg/dL", "HIGH"),
    ]
    
    y_pos -= 20
    for test, value, range_val, unit, status in lipid_results:
        if status in ["HIGH", "LOW"]:
            c.setFont("Helvetica-Bold", 10)
        else:
            c.setFont("Helvetica", 10)
        c.drawString(70, y_pos, f"{test}: {value} {unit} (Normal: {range_val}) - {status}")
        y_pos -= 15
    
    # Glucose - slightly elevated
    y_pos -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y_pos, "Glucose Metabolism")
    
    c.setFont("Helvetica-Bold", 10)
    y_pos -= 20
    c.drawString(70, y_pos, "Fasting Glucose: 108 mg/dL (Normal: 70-100) - SLIGHTLY HIGH")
    c.drawString(70, y_pos - 15, "HbA1c: 6.2% (Normal: <5.7%) - PREDIABETIC RANGE")
    
    # Iron studies - low
    y_pos -= 50
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y_pos, "Iron Studies")
    
    c.setFont("Helvetica", 10)
    iron_results = [
        ("Hemoglobin", "10.8", "12.0-16.0", "g/dL", "LOW"),
        ("Iron", "45", "60-170", "mcg/dL", "LOW"),
        ("Ferritin", "12", "15-150", "ng/mL", "LOW"),
    ]
    
    y_pos -= 20
    for test, value, range_val, unit, status in iron_results:
        if status == "LOW":
            c.setFont("Helvetica-Bold", 10)
        else:
            c.setFont("Helvetica", 10)
        c.drawString(70, y_pos, f"{test}: {value} {unit} (Normal: {range_val}) - {status}")
        y_pos -= 15
    
    # Recommendations
    y_pos -= 40
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y_pos, "RECOMMENDATIONS:")
    
    c.setFont("Helvetica", 10)
    recommendations = [
        "• Follow up with physician within 2 weeks",
        "• Consider dietary modifications for cholesterol management",
        "• Evaluate for iron deficiency anemia",
        "• Lifestyle counseling for diabetes prevention",
        "• Repeat labs in 3 months"
    ]
    
    y_pos -= 20
    for rec in recommendations:
        c.drawString(70, y_pos, rec)
        y_pos -= 15
    
    c.save()
    print(f"✅ Created abnormal blood test report: {filename}")
    return filename

def main():
    """Create sample blood test files"""
    print("Creating Sample Blood Test Data")
    print("=" * 40)
    
    try:
        # Create comprehensive normal report
        normal_file = create_comprehensive_blood_test()
        
        # Create abnormal report
        abnormal_file = create_abnormal_blood_test()
        
        print("\n🎉 Sample files created successfully!")
        print(f"Normal results: {normal_file}")
        print(f"Abnormal results: {abnormal_file}")
        print("\nYou can now test the API with these files using:")
        print("python scripts/manual_test.py")
        
    except Exception as e:
        print(f"❌ Error creating sample files: {e}")

if __name__ == "__main__":
    main()

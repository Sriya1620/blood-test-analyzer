#!/usr/bin/env python3
"""
Test script for the Blood Test Report Analyzer API
"""

import requests
import os

def test_health_check():
    """Test the health check endpoint"""
    try:
        response = requests.get("http://localhost:8000/")
        print("Health Check Response:")
        print(response.json())
        return response.status_code == 200
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

def test_detailed_health():
    """Test the detailed health endpoint"""
    try:
        response = requests.get("http://localhost:8000/health")
        print("\nDetailed Health Response:")
        print(response.json())
        return response.status_code == 200
    except Exception as e:
        print(f"Detailed health check failed: {e}")
        return False

def create_sample_pdf():
    """Create a sample PDF for testing"""
    try:
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter
        
        filename = "sample_blood_test.pdf"
        c = canvas.Canvas(filename, pagesize=letter)
        
        # Add sample blood test content
        c.drawString(100, 750, "BLOOD TEST REPORT")
        c.drawString(100, 720, "Patient: John Doe")
        c.drawString(100, 700, "Date: 2024-01-15")
        c.drawString(100, 680, "Laboratory: Sample Lab")
        
        c.drawString(100, 640, "TEST RESULTS:")
        c.drawString(100, 620, "Glucose: 95 mg/dL (Normal: 70-100)")
        c.drawString(100, 600, "Cholesterol: 180 mg/dL (Normal: <200)")
        c.drawString(100, 580, "HDL: 45 mg/dL (Normal: >40)")
        c.drawString(100, 560, "LDL: 120 mg/dL (Normal: <130)")
        c.drawString(100, 540, "Hemoglobin: 14.5 g/dL (Normal: 12-16)")
        
        c.save()
        return filename
    except ImportError:
        print("reportlab not installed. Creating a simple text file instead.")
        filename = "sample_blood_test.txt"
        with open(filename, 'w') as f:
            f.write("""BLOOD TEST REPORT
Patient: John Doe
Date: 2024-01-15
Laboratory: Sample Lab

TEST RESULTS:
Glucose: 95 mg/dL (Normal: 70-100)
Cholesterol: 180 mg/dL (Normal: <200)
HDL: 45 mg/dL (Normal: >40)
LDL: 120 mg/dL (Normal: <130)
Hemoglobin: 14.5 g/dL (Normal: 12-16)
""")
        return filename

def test_file_upload():
    """Test file upload and analysis"""
    # Create sample file
    sample_file = create_sample_pdf()
    
    try:
        with open(sample_file, 'rb') as f:
            files = {'file': (sample_file, f, 'application/pdf')}
            data = {
                'query': 'Please analyze my blood test results',
                'analysis_type': 'verification'
            }
            
            response = requests.post(
                "http://localhost:8000/analyze",
                files=files,
                data=data
            )
            
            print(f"\nFile Upload Response (Status: {response.status_code}):")
            if response.status_code == 200:
                result = response.json()
                print(f"Status: {result.get('status')}")
                print(f"Query: {result.get('query')}")
                print(f"Analysis Type: {result.get('analysis_type')}")
                print(f"File Processed: {result.get('file_processed')}")
                print("Analysis Preview:", result.get('analysis', '')[:200] + "...")
            else:
                print("Error:", response.text)
                
        return response.status_code == 200
        
    except Exception as e:
        print(f"File upload test failed: {e}")
        return False
    finally:
        # Clean up sample file
        if os.path.exists(sample_file):
            os.remove(sample_file)

def main():
    """Run all tests"""
    print("Testing Blood Test Report Analyzer API")
    print("=" * 50)
    
    tests = [
        ("Health Check", test_health_check),
        ("Detailed Health", test_detailed_health),
        ("File Upload", test_file_upload)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\nRunning {test_name}...")
        result = test_func()
        results.append((test_name, result))
        print(f"{test_name}: {'PASSED' if result else 'FAILED'}")
    
    print("\n" + "=" * 50)
    print("TEST SUMMARY:")
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name}: {status}")

if __name__ == "__main__":
    main()

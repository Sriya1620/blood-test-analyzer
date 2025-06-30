#!/usr/bin/env python3
"""
🧪 Complete test suite for Blood Test Analyzer
"""

import requests
import os
import time
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_test_pdf():
    """Create a test blood test PDF"""
    filename = "test_blood_report.pdf"
    
    c = canvas.Canvas(filename, pagesize=letter)
    
    # Add content
    c.drawString(100, 750, "BLOOD TEST REPORT")
    c.drawString(100, 720, "Patient: Test Patient")
    c.drawString(100, 700, "Date: 2024-01-15")
    c.drawString(100, 680, "Laboratory: Test Lab")
    
    c.drawString(100, 640, "TEST RESULTS:")
    c.drawString(100, 620, "Glucose: 95 mg/dL (Normal: 70-100)")
    c.drawString(100, 600, "Total Cholesterol: 180 mg/dL (Normal: <200)")
    c.drawString(100, 580, "HDL Cholesterol: 45 mg/dL (Normal: >40)")
    c.drawString(100, 560, "LDL Cholesterol: 120 mg/dL (Normal: <130)")
    c.drawString(100, 540, "Triglycerides: 110 mg/dL (Normal: <150)")
    c.drawString(100, 520, "Hemoglobin: 14.5 g/dL (Normal: 12-16)")
    c.drawString(100, 500, "White Blood Cells: 7.2 K/uL (Normal: 4.0-11.0)")
    
    c.save()
    return filename

def test_health_endpoints():
    """Test health check endpoints"""
    print("🏥 Testing Health Endpoints...")
    
    try:
        # Test basic health
        response = requests.get("http://localhost:8000/")
        print(f"✅ Basic Health Check: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Message: {data.get('message', 'N/A')}")
            print(f"   Status: {data.get('status', 'N/A')}")
        
        # Test detailed health
        response = requests.get("http://localhost:8000/health")
        print(f"✅ Detailed Health Check: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"   Service: {data.get('service', 'N/A')}")
            print(f"   Ready: {data.get('ready_for_analysis', 'N/A')}")
        
        return True
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure it's running!")
        return False
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False

def test_file_analysis(analysis_type="comprehensive"):
    """Test file upload and analysis"""
    print(f"\n🔬 Testing {analysis_type.title()} Analysis...")
    
    # Create test PDF
    pdf_file = create_test_pdf()
    
    try:
        with open(pdf_file, 'rb') as f:
            files = {'file': (pdf_file, f, 'application/pdf')}
            data = {
                'query': f'Please provide a {analysis_type} analysis of my blood test results',
                'analysis_type': analysis_type
            }
            
            print(f"📤 Uploading {pdf_file}...")
            response = requests.post(
                "http://localhost:8000/analyze",
                files=files,
                data=data,
                timeout=60
            )
            
            print(f"📥 Response Status: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                print("✅ Analysis completed successfully!")
                print(f"   Status: {result.get('status')}")
                print(f"   Query: {result.get('query')}")
                print(f"   Analysis Type: {result.get('analysis_type')}")
                print(f"   File Processed: {result.get('file_processed')}")
                print(f"   Model Used: {result.get('model_used')}")
                print("   Analysis Preview:")
                analysis = result.get('analysis', '')
                print("   " + analysis[:300] + "..." if len(analysis) > 300 else analysis)
                return True
            else:
                print(f"❌ Analysis failed: {response.text}")
                return False
                
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False
    finally:
        # Clean up
        if os.path.exists(pdf_file):
            os.remove(pdf_file)

def run_all_tests():
    """Run complete test suite"""
    print("🧪 BLOOD TEST ANALYZER - COMPLETE TEST SUITE")
    print("=" * 60)
    
    tests = [
        ("Health Endpoints", test_health_endpoints),
        ("Comprehensive Analysis", lambda: test_file_analysis("comprehensive")),
        ("Nutrition Analysis", lambda: test_file_analysis("nutrition")),
        ("Exercise Analysis", lambda: test_file_analysis("exercise")),
        ("Document Verification", lambda: test_file_analysis("verification"))
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n{'='*20} {test_name} {'='*20}")
        try:
            result = test_func()
            results.append((test_name, result))
            status = "✅ PASSED" if result else "❌ FAILED"
            print(f"\n{test_name}: {status}")
        except Exception as e:
            print(f"\n❌ {test_name}: FAILED - {e}")
            results.append((test_name, False))
        
        time.sleep(1)  # Brief pause between tests
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name:<25}: {status}")
    
    print(f"\n🎯 OVERALL RESULT: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! Your Blood Test Analyzer is working perfectly!")
    else:
        print("⚠️  Some tests failed. Check the server logs for details.")

if __name__ == "__main__":
    print("⏳ Waiting for server to start...")
    time.sleep(3)
    run_all_tests()

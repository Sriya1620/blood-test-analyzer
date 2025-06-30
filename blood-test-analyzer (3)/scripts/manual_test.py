#!/usr/bin/env python3
"""
Manual test script for uploading your own blood test PDF
"""

import requests
import os

def test_manual_upload(pdf_path, query="Analyze my blood test results", analysis_type="comprehensive"):
    """Test with your own PDF file"""
    
    if not os.path.exists(pdf_path):
        print(f"Error: File not found at {pdf_path}")
        return False
    
    try:
        with open(pdf_path, 'rb') as f:
            files = {'file': (os.path.basename(pdf_path), f, 'application/pdf')}
            data = {
                'query': query,
                'analysis_type': analysis_type
            }
            
            print(f"Uploading {pdf_path}...")
            print(f"Query: {query}")
            print(f"Analysis Type: {analysis_type}")
            print("-" * 50)
            
            response = requests.post(
                "http://localhost:8000/analyze",
                files=files,
                data=data,
                timeout=300  # 5 minute timeout for AI processing
            )
            
            if response.status_code == 200:
                result = response.json()
                print("✅ SUCCESS!")
                print(f"Status: {result.get('status')}")
                print(f"File Processed: {result.get('file_processed')}")
                print(f"Analysis Type: {result.get('analysis_type')}")
                print("\n" + "="*50)
                print("ANALYSIS RESULTS:")
                print("="*50)
                print(result.get('analysis', 'No analysis returned'))
                print("\n" + "="*50)
                print("DISCLAIMER:")
                print(result.get('disclaimer', ''))
                return True
            else:
                print(f"❌ ERROR (Status: {response.status_code})")
                print("Response:", response.text)
                return False
                
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def main():
    """Main function to run manual tests"""
    print("Manual Blood Test PDF Upload Test")
    print("=" * 50)
    
    # Example usage - replace with your actual PDF path
    pdf_path = input("Enter path to your blood test PDF: ").strip()
    
    if not pdf_path:
        print("No file path provided. Exiting.")
        return
    
    # Get user preferences
    query = input("Enter your question (or press Enter for default): ").strip()
    if not query:
        query = "Provide a comprehensive analysis of my blood test report"
    
    print("\nAnalysis Types:")
    print("1. comprehensive (default) - Full analysis with all specialists")
    print("2. nutrition - Focus on nutrition recommendations")
    print("3. exercise - Focus on exercise planning")
    print("4. verification - Document verification only")
    
    analysis_choice = input("Choose analysis type (1-4, or press Enter for default): ").strip()
    analysis_types = {
        "1": "comprehensive",
        "2": "nutrition", 
        "3": "exercise",
        "4": "verification"
    }
    analysis_type = analysis_types.get(analysis_choice, "comprehensive")
    
    # Run the test
    success = test_manual_upload(pdf_path, query, analysis_type)
    
    if success:
        print("\n🎉 Test completed successfully!")
    else:
        print("\n💥 Test failed. Check the error messages above.")

if __name__ == "__main__":
    main()

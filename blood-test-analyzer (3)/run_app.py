#!/usr/bin/env python3
"""
🚀 One-click launcher for Blood Test Analyzer
Just run: python run_app.py
"""

import subprocess
import sys
import os
import time

def check_and_install_requirements():
    """Install required packages"""
    print("📦 Checking and installing requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements_working.txt"])
        print("✅ All requirements installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False

def create_data_directory():
    """Create data directory if it doesn't exist"""
    if not os.path.exists("data"):
        os.makedirs("data")
        print("📁 Created data directory")

def run_server():
    """Run the FastAPI server"""
    print("\n🚀 Starting Blood Test Report Analyzer...")
    print("=" * 50)
    print("📍 Server URL: http://localhost:8000")
    print("📚 API Docs: http://localhost:8000/docs")
    print("🩺 Ready to analyze blood test reports!")
    print("=" * 50)
    print("\n⏹️  Press Ctrl+C to stop the server")
    print("\n🔄 Starting server...")
    
    try:
        # Import and run the app
        from main_working import app
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped. Thank you for using Blood Test Analyzer!")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        print("💡 Try running: python main_working.py")

def main():
    """Main function"""
    print("🩺 Blood Test Report Analyzer - One-Click Setup")
    print("=" * 50)
    
    # Step 1: Install requirements
    if not check_and_install_requirements():
        print("❌ Failed to install requirements. Please check your internet connection.")
        return
    
    # Step 2: Create directories
    create_data_directory()
    
    # Step 3: Wait a moment
    print("\n⏳ Preparing to start server...")
    time.sleep(2)
    
    # Step 4: Run server
    run_server()

if __name__ == "__main__":
    main()

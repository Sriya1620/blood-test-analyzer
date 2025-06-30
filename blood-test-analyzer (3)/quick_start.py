#!/usr/bin/env python3
"""
🚀 QUICK START - Blood Test Analyzer
Just run: python quick_start.py
"""

import subprocess
import sys
import os
import time

def install_requirements():
    """Install simplified requirements"""
    print("📦 Installing requirements...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", 
            "-r", "requirements_simple.txt"
        ])
        print("✅ Requirements installed!")
        return True
    except Exception as e:
        print(f"❌ Installation failed: {e}")
        return False

def setup_environment():
    """Setup environment"""
    print("🔧 Setting up environment...")
    
    # Create .env file
    env_content = "PYTHONPATH=.\n"
    with open(".env", "w") as f:
        f.write(env_content)
    
    # Create data directory
    os.makedirs("data", exist_ok=True)
    
    print("✅ Environment ready!")

def run_server():
    """Run the server"""
    print("\n🚀 Starting Blood Test Analyzer...")
    print("=" * 50)
    print("📍 Server: http://localhost:8000")
    print("📚 API Docs: http://localhost:8000/docs")
    print("🩺 Ready to analyze blood tests!")
    print("=" * 50)
    print("\n⏹️  Press Ctrl+C to stop")
    
    try:
        subprocess.run([sys.executable, "main_simple.py"])
    except KeyboardInterrupt:
        print("\n👋 Server stopped!")

def main():
    """Main function"""
    print("🩺 BLOOD TEST ANALYZER - QUICK START")
    print("=" * 50)
    
    if not install_requirements():
        return
    
    setup_environment()
    
    print("\n⏳ Starting in 3 seconds...")
    time.sleep(3)
    
    run_server()

if __name__ == "__main__":
    main()

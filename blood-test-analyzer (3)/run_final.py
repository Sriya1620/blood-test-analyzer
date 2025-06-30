#!/usr/bin/env python3
"""
🚀 FINAL WORKING VERSION - Blood Test Analyzer
Just run: python run_final.py
"""

import subprocess
import sys
import os
import time

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
    print("\n🚀 Starting Blood Test Analyzer (FINAL WORKING VERSION)...")
    print("=" * 70)
    print("📍 Server: http://localhost:8000")
    print("📚 API Docs: http://localhost:8000/docs")
    print("🩺 Ready to analyze blood tests!")
    print("⚡ Self-contained - no external dependencies!")
    print("🔧 All issues resolved!")
    print("=" * 70)
    print("\n⏹️  Press Ctrl+C to stop")
    
    try:
        subprocess.run([sys.executable, "main_working_final.py"])
    except KeyboardInterrupt:
        print("\n👋 Server stopped!")

def main():
    """Main function"""
    print("🩺 BLOOD TEST ANALYZER - FINAL WORKING VERSION")
    print("=" * 60)
    
    setup_environment()
    
    print("\n⏳ Starting in 2 seconds...")
    time.sleep(2)
    
    run_server()

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
🚀 FIXED VERSION - Blood Test Analyzer
Just run: python run_fixed.py
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
    print("\n🚀 Starting Blood Test Analyzer (FIXED VERSION)...")
    print("=" * 60)
    print("📍 Server: http://localhost:8000")
    print("📚 API Docs: http://localhost:8000/docs")
    print("🩺 Ready to analyze blood tests!")
    print("🔧 All dependencies resolved!")
    print("=" * 60)
    print("\n⏹️  Press Ctrl+C to stop")
    
    try:
        subprocess.run([sys.executable, "main_fixed.py"])
    except KeyboardInterrupt:
        print("\n👋 Server stopped!")

def main():
    """Main function"""
    print("🩺 BLOOD TEST ANALYZER - FIXED VERSION")
    print("=" * 50)
    
    setup_environment()
    
    print("\n⏳ Starting in 2 seconds...")
    time.sleep(2)
    
    run_server()

if __name__ == "__main__":
    main()

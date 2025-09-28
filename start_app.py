#!/usr/bin/env python3
"""
Startup script for the INGRES AI Chatbot application.
This script will start all necessary services and populate the database.
"""

import subprocess
import sys
import time
import os
from pathlib import Path

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False

def check_docker():
    """Check if Docker is running."""
    try:
        subprocess.run("docker --version", shell=True, check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    """Main startup function."""
    print("🚀 Starting INGRES AI Chatbot Application")
    print("=" * 50)
    
    # Check if Docker is available
    if not check_docker():
        print("❌ Docker is not installed or not running.")
        print("Please install Docker Desktop and try again.")
        return
    
    # Create static directory if it doesn't exist
    static_dir = Path("static")
    static_dir.mkdir(exist_ok=True)
    
    # Start Docker services
    print("\n🐳 Starting Docker services...")
    if not run_command("docker-compose up -d postgres qdrant", "Starting PostgreSQL and Qdrant"):
        print("❌ Failed to start Docker services")
        return
    
    # Wait for services to be ready
    print("\n⏳ Waiting for services to be ready...")
    time.sleep(10)
    
    # Install Python dependencies
    print("\n📦 Installing Python dependencies...")
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        print("❌ Failed to install dependencies")
        return
    
    # Populate database with dummy data
    print("\n📊 Setting up dummy database...")
    if not run_command("python populate_dummy_data.py", "Populating database"):
        print("❌ Failed to populate database")
        return
    
    print("\n🎉 Setup complete!")
    print("\n" + "=" * 50)
    print("🚀 Your INGRES AI Chatbot is ready!")
    print("\nTo start the application, run one of these commands:")
    print("\n1. Start the backend API:")
    print("   python server.py")
    print("\n2. Start the frontend UI (in a new terminal):")
    print("   streamlit run app.py")
    print("\n3. Or use Docker for everything:")
    print("   docker-compose up")
    print("\n📱 The application will be available at:")
    print("   - Frontend: http://localhost:8501")
    print("   - Backend API: http://localhost:8000")
    print("   - Qdrant: http://localhost:6333")
    print("   - PostgreSQL: localhost:5432")

if __name__ == "__main__":
    main()

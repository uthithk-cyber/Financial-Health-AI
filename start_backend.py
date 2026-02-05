#!/usr/bin/env python
"""Quick backend runner"""
import sys
import os

# Add backend to path
sys.path.insert(0, os.path.dirname(__file__))

if __name__ == "__main__":
    from backend.main import app
    import uvicorn
    print("🚀 Starting Financial Health AI Backend...")
    print("📍 Server: http://127.0.0.1:8000")
    print("📚 API Docs: http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import sys
from pathlib import Path
import logging
from datetime import datetime
import streamlit as st


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Add backend to path
backend_dir = Path(__file__).resolve().parent
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

from routes.analysis import router as analysis_router

app = FastAPI(
    title="SME Financial Health Assessment Platform",
    description="AI-powered financial analysis for small and medium enterprises",
    version="1.0.0"
)

# CORS middleware configuration
cors_origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:8000",
    "*"  # Development: allow all origins
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analysis_router)


@app.get("/")
def root():
    """Root endpoint - check if backend is running"""
    return {
        "status": "online",
        "service": "SME Financial Health Assessment Platform",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat()
    }


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }


@app.on_event("startup")
async def startup_event():
    """Startup event handler"""
    logger.info("[backend] SME Financial Health Platform started successfully")
    logger.info(f"[backend] CORS enabled for origins: {cors_origins}")
    print("[backend] ✓ FastAPI server running on http://localhost:8000")
    print("[backend] ✓ API Docs available at http://localhost:8000/docs")


@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event handler"""
    logger.info("[backend] SME Financial Health Platform shutting down")


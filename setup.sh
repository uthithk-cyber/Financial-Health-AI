#!/bin/bash

# Quick Start Script for SME Financial Health Assessment Platform
# Usage: bash setup.sh

echo ""
echo "===================================================================="
echo "  SME Financial Health Assessment Platform - Quick Start"
echo "===================================================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.9+ from https://www.python.org/"
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "ERROR: Node.js is not installed"
    echo "Please install Node.js from https://nodejs.org/"
    exit 1
fi

echo ""
echo "Step 1: Checking Python version..."
python3 --version

echo ""
echo "Step 2: Checking Node.js version..."
node --version

echo ""
echo "Step 3: Creating/Activating backend virtual environment..."
cd backend || exit 1

if [ ! -d "venv" ]; then
    echo "Creating new virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

echo ""
echo "Step 4: Installing backend dependencies..."
pip install -r requirements.txt -q

echo ""
echo "Step 5: Installing frontend dependencies..."
cd ../frontend || exit 1

if [ ! -d "node_modules" ]; then
    echo "Installing npm packages (this may take a minute)..."
    npm install --silent
else
    echo "npm packages already installed"
fi

cd ..

echo ""
echo "===================================================================="
echo "  SETUP COMPLETE!"
echo "===================================================================="
echo ""
echo "To start the application:"
echo ""
echo "Terminal 1 - Start Backend:"
echo "  cd backend"
echo "  source venv/bin/activate"
echo "  python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000"
echo ""
echo "Terminal 2 - Start Frontend:"
echo "  cd frontend"
echo "  npm start"
echo ""
echo "Then open your browser to: http://localhost:3000"
echo ""
echo "API Documentation: http://localhost:8000/docs"
echo ""

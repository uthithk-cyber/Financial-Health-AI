@echo off
REM Quick Start Script for SME Financial Health Assessment Platform
REM This batch file helps with Windows development setup

echo.
echo ====================================================================
echo  SME Financial Health Assessment Platform - Quick Start
echo ====================================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.9+ from https://www.python.org/
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed or not in PATH
    echo Please install Node.js from https://nodejs.org/
    pause
    exit /b 1
)

echo.
echo Step 1: Checking Python version...
python --version

echo.
echo Step 2: Checking Node.js version...
node --version

echo.
echo Step 3: Creating/Activating backend virtual environment...
cd backend
if not exist venv (
    echo Creating new virtual environment...
    python -m venv venv
)
call venv\Scripts\activate.bat

echo.
echo Step 4: Installing backend dependencies...
pip install -r requirements.txt --quiet

echo.
echo Step 5: Installing frontend dependencies...
cd ..\frontend
if not exist node_modules (
    echo Installing npm packages (this may take a minute)...
    call npm install --silent
) else (
    echo npm packages already installed
)

cd ..

echo.
echo ====================================================================
echo  SETUP COMPLETE!
echo ====================================================================
echo.
echo To start the application:
echo.
echo Terminal 1 - Start Backend:
echo   cd backend
echo   venv\Scripts\activate
echo   python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
echo.
echo Terminal 2 - Start Frontend:
echo   cd frontend
echo   npm start
echo.
echo Then open your browser to: http://localhost:3000
echo.
echo API Documentation: http://localhost:8000/docs
echo.
pause

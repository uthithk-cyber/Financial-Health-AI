@echo off
REM Start Financial Health Assessment Tool

echo ================================
echo Financial Health Assessment Tool
echo ================================
echo.
echo Starting Backend Server...
echo.

start "Backend Server" cmd /k "cd /d e:\financial-health-ai && E:/financial-health-ai/.venv/Scripts/python.exe -m uvicorn backend.main:app --host 127.0.0.1 --port 8000"

timeout /t 3

echo.
echo Starting Frontend...
echo.

start "Frontend" cmd /k "cd /d e:\financial-health-ai\frontend && npm start"

timeout /t 3

echo.
echo ================================
echo BACKEND: http://127.0.0.1:8000
echo API DOCS: http://127.0.0.1:8000/docs
echo FRONTEND: http://localhost:3000
echo ================================
echo.
pause

#!/usr/bin/env python
"""
Run the FastAPI backend with proper Windows event loop handling
"""
import asyncio
import sys
import os
from pathlib import Path

# Set event loop policy for Windows
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Run uvicorn
if __name__ == "__main__":
    import uvicorn
    import os
    
    backend_dir = Path(__file__).resolve().parent / "backend"
    sys.path.insert(0, str(backend_dir))
    os.chdir(str(backend_dir))
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

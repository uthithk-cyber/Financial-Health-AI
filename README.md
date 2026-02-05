SME Financial Health — Submission README

Project summary
- Simple demo that analyzes SME financial health from a CSV and provides three layers of output:
  - Layer 1: Raw SME row data (hidden by default; available via `show_raw=true`)
  - Layer 2: Computed financial metrics (SME-scoped when `business_id` is provided)
  - Layer 3: AI-driven recommendations (SME-aware)

What9s included
- backend/ : FastAPI backend
- frontend/ : React frontend and static demo in `public/index.html`
- backend/sample_data/SME_Financial_Health_Dataset.csv : demo dataset

Quick start (development)
1) Backend: install Python requirements and run uvicorn

Windows PowerShell (recommended - run as Administrator for firewall rule):

```powershell
cd D:\financial-health-ai\backend
python -m pip install -r requirements.txt
# Allow remote access (only if remote judges need to reach your machine)
# Run in elevated PowerShell:
# New-NetFirewallRule -DisplayName "Allow Uvicorn 8000" -Direction Inbound -LocalPort 8000 -Protocol TCP -Action Allow
# Or in elevated CMD:
# netsh advfirewall firewall add rule name="Allow Uvicorn 8000" dir=in action=allow protocol=TCP localport=8000

# Start the server (from project root recommended):
cd ..
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

2) Frontend (development):
```bash
cd frontend
npm install
npm start
# opens at http://localhost:3000 (or alternate port if occupied)
```

3) Frontend (production build):
```bash
cd frontend
npm run build
# serve build folder (example):
npx serve -s build
```

Endpoints
- GET /analysis : dataset-level metrics
- GET /analysis?business_id=SME_1 : SME-scoped metrics (no raw returned by default)
- GET /analysis?business_id=SME_1&show_raw=true : include raw SME row
- GET /analysis/smes : list of SME ids for autocomplete

Notes for judges / reviewers
- For presentation clarity, raw SME rows are hidden by default. Use the "Show raw" toggle in the UI or `show_raw=true` in the querystring to view Layer 1.
- The AI recommendations are deterministic heuristics in `backend/ai_engine.py` and are suitable for demo use. Replace with a real model or LLM integration for production.

Files changed by the developer assistant
- backend/main.py: robust import + startup print
- backend/routes/analysis.py: async, show_raw flag, tolerant SME matching, robust imports
- backend/financial_analysis.py: SME-scoped metrics
- backend/ai_engine.py: SME-aware recommendations
- frontend/src/components/Dashboard.jsx: modern UI, Show raw, Export/Print
- frontend/src/components/Dashboard.css: new styling
- frontend/public/index.html: styled static demo, Show raw, Export/Print

Submission checklist
- [ ] Confirm `python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000` is running and accessible from judges' network (if needed)
- [ ] Serve `frontend/build` (or run dev server) and confirm demo works
- [ ] Include this README.md in your submission

Contact
- If any issues occur while running, paste server logs or browser DevTools Network errors and I will help fix them quickly.

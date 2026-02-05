# 🚀 QUICK REFERENCE CARD

## One-Command Setup (Windows)
```bash
cd e:\financial-health-ai && setup.bat
```

## One-Command Setup (Mac/Linux)
```bash
cd financial-health-ai && bash setup.sh
```

---

## Starting the Application

**Terminal 1 (Backend):**
```bash
cd backend
venv\Scripts\activate
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 (Frontend):**
```bash
cd frontend
npm start
```

**Browser:**
```
http://localhost:3000
```

---

## API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Check if backend is running |
| `/health` | GET | Health check |
| `/analysis/` | GET | Analyze all or specific SME |
| `/analysis/smes` | GET | List available SME IDs |
| `/docs` | GET | Interactive API documentation |

---

## Query Parameters for /analysis/

```
?business_id=SME_1      # Analyze specific SME
?show_raw=true          # Include raw row data
```

---

## Test with curl

```bash
# Health check
curl http://localhost:8000/health

# Analyze all SMEs
curl http://localhost:8000/analysis/

# Analyze SME_1
curl "http://localhost:8000/analysis/?business_id=SME_1"

# With raw data
curl "http://localhost:8000/analysis/?business_id=SME_1&show_raw=true"

# List SMEs
curl http://localhost:8000/analysis/smes
```

---

## Key Files

| File | Purpose |
|------|---------|
| `backend/main.py` | FastAPI application |
| `backend/financial_analysis.py` | Metrics calculation |
| `backend/ai_engine.py` | AI recommendations |
| `frontend/src/components/Dashboard.jsx` | React UI |
| `frontend/src/components/Dashboard.css` | Styling |
| `.env.example` | Configuration template |

---

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Port 8000 in use | Change port: `--port 8001` |
| Port 3000 in use | `PORT=3001 npm start` |
| Module not found | Run `pip install -r requirements.txt` |
| API not found | Ensure backend is running |
| No data | Check CSV file exists in `backend/sample_data/` |

---

## Documentation Files

- **SETUP_GUIDE.md** - Complete setup instructions
- **TESTING_GUIDE.md** - Testing procedures
- **COMPLETE_SOLUTION.md** - Summary of all changes

---

## Expected Response Format

```json
{
  "rows": 1,
  "columns": [...],
  "metrics": {
    "annual_revenue": 34999221,
    "total_expenses": 26355176,
    "profit": 8644045,
    "profit_margin": 24.7,
    "cash_health_ratio": 2.63,
    "risk_level": "Low Risk",
    "financial_health_score": 100
  },
  "ai_recommendations": [
    "Recommendation 1",
    "Recommendation 2"
  ],
  "raw": null
}
```

---

## Risk Level Colors

- 🟢 **Low Risk** - Green: #dcfce7
- 🟡 **Medium Risk** - Orange: #fef3c7
- 🔴 **High Risk** - Red: #fee2e2

---

## Environment Variables

```env
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000
DATABASE_URL=postgresql://user:pass@localhost:5432/sme_finance
OPENAI_API_KEY=sk-xxx
DEBUG=False
```

---

## Success Checklist

✅ Backend running on port 8000
✅ Frontend running on port 3000
✅ Can access http://localhost:3000
✅ Can search for SME_1
✅ Metrics display correctly
✅ Recommendations appear
✅ No console errors
✅ API health shows "online"

---

## Keyboard Shortcuts

- **Enter** - Submit search (from search box)
- **Ctrl+P** - Print/Export (works anywhere)
- **F12** - Developer tools (for debugging)

---

## File Structure

```
financial-health-ai/
├── backend/
│   ├── main.py
│   ├── financial_analysis.py
│   ├── ai_engine.py
│   ├── requirements.txt
│   ├── routes/analysis.py
│   └── sample_data/SME_Financial_Health_Dataset.csv
├── frontend/
│   ├── package.json
│   ├── public/index.html
│   └── src/components/Dashboard.jsx
├── .env.example
├── setup.bat
├── setup.sh
├── SETUP_GUIDE.md
├── TESTING_GUIDE.md
└── COMPLETE_SOLUTION.md
```

---

## Version Info

- **Backend**: FastAPI 0.104.1
- **Frontend**: React 18.2.0
- **Python**: 3.9+
- **Node.js**: 14+

---

## Support

1. Check SETUP_GUIDE.md for detailed instructions
2. Check TESTING_GUIDE.md for testing procedures
3. Visit http://localhost:8000/docs for API docs
4. Check browser console (F12) for errors
5. Check backend terminal for logs

---

## 🎯 Success = Working App!

When you see:
- ✅ Backend running
- ✅ Frontend loaded
- ✅ Metrics displayed
- ✅ Recommendations shown
- ✅ No errors

**You're ready to go! 🚀**

---

**Last Updated:** February 3, 2026
**Status:** Complete & Working ✅

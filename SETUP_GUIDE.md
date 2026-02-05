# Financial Health Assessment Platform for SMEs

**AI-powered financial analysis and recommendations for Small & Medium Enterprises**

## 🎯 Overview

A comprehensive platform that uses advanced AI to analyze financial health, identify risks, suggest cost optimization strategies, and recommend suitable financial products for SMEs. The system evaluates creditworthiness, provides actionable insights, and supports multiple business types with industry-specific benchmarking.

### Key Features
- 📊 **Financial Analysis**: Revenue, expenses, profit, cash health metrics
- 🤖 **AI Recommendations**: Personalized financial optimization suggestions
- 📈 **Risk Assessment**: High/Medium/Low risk categorization
- 💰 **Multiple Data Sources**: CSV/XLSX upload support
- 🌐 **Industry-Specific Insights**: Tailored for different business types
- 🔒 **Secure**: Encrypted data handling
- 📱 **Responsive UI**: Works on desktop and mobile
- 🚀 **Fast Processing**: Real-time analysis with async processing

---

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI (Python 3.9+)
- **Data Processing**: Pandas, NumPy
- **Database**: PostgreSQL (optional)
- **AI/ML**: OpenAI GPT integration
- **Security**: encryption, CORS, JWT tokens

### Frontend
- **Library**: React 18
- **Styling**: Modern CSS with gradients
- **HTTP Client**: Axios
- **Build**: Create React App

### Infrastructure
- **Development Server**: Uvicorn (FastAPI)
- **Port Configuration**: Backend on 8000, Frontend on 3000

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.9 or higher
- Node.js 14+ and npm
- Git

### Step 1: Clone and Navigate
```bash
cd e:\financial-health-ai
```

### Step 2: Backend Setup

#### 2.1 Create Virtual Environment
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Mac/Linux
```

#### 2.2 Install Dependencies
```bash
pip install -r requirements.txt
```

#### 2.3 Environment Configuration
Copy `.env.example` to `.env` and update values:
```bash
copy .env.example .env  # Windows
# or
cp .env.example .env  # Mac/Linux
```

Edit `.env` with your settings:
```env
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000
OPENAI_API_KEY=sk-your-key-here  # Optional, only if using GPT
DATABASE_URL=postgresql://user:password@localhost:5432/sme_finance
DEBUG=False
```

#### 2.4 Start Backend Server
```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Expected output:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

### Step 3: Frontend Setup

#### 3.1 Navigate to Frontend
```bash
cd ../frontend
```

#### 3.2 Install Dependencies
```bash
npm install
```

#### 3.3 Environment Configuration (Optional)
Create `.env` file in `frontend/`:
```env
REACT_APP_API_URL=http://localhost:8000
```

#### 3.4 Start Frontend Development Server
```bash
npm start
```

Expected output:
```
Compiled successfully!
You can now view sme-finance-ui in the browser.
  Local:            http://localhost:3000
  On Your Network:  http://[your-ip]:3000
```

---

## 🚀 Running the Application

### Complete Startup Sequence

**Terminal 1 - Backend:**
```bash
cd e:\financial-health-ai\backend
venv\Scripts\activate
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Frontend:**
```bash
cd e:\financial-health-ai\frontend
npm start
```

**Browser:**
- Navigate to `http://localhost:3000`
- Backend API: `http://localhost:8000`
- API Documentation: `http://localhost:8000/docs`

---

## 📊 API Endpoints

### Core Analysis Endpoints

#### 1. Get Financial Analysis
```
GET /analysis/
Query Parameters:
  - business_id (optional): Filter by specific SME
  - show_raw (optional): Include raw dataset row

Example:
GET /analysis/?business_id=SME_1&show_raw=true

Response:
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
    "financial_health_score": 100,
    "debt_equity_ratio": 2.4
  },
  "ai_recommendations": [
    "Monitor cash conversion cycle...",
    "Eligible for growth investment..."
  ],
  "raw": { ... }
}
```

#### 2. List Available SMEs
```
GET /analysis/smes

Response:
{
  "smes": ["SME_1", "SME_2", "SME_3", ...]
}
```

#### 3. Health Check
```
GET /health

Response:
{
  "status": "healthy",
  "timestamp": "2026-02-03T10:30:00"
}
```

#### 4. Root Endpoint
```
GET /

Response:
{
  "status": "online",
  "service": "SME Financial Health Assessment Platform",
  "version": "1.0.0",
  "timestamp": "2026-02-03T10:30:00"
}
```

---

## 📁 Project Structure

```
financial-health-ai/
├── backend/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app & server config
│   ├── ai_engine.py            # AI recommendation logic
│   ├── financial_analysis.py   # Financial metrics computation
│   ├── requirements.txt        # Python dependencies
│   ├── sample_data/
│   │   └── SME_Financial_Health_Dataset.csv
│   └── routes/
│       ├── __init__.py
│       └── analysis.py         # API endpoint definitions
│
├── frontend/
│   ├── package.json
│   ├── public/
│   │   └── index.html
│   └── src/
│       ├── App.js
│       ├── index.js
│       └── components/
│           ├── Dashboard.jsx   # Main UI component
│           └── Dashboard.css   # Styles
│
├── database/
│   └── schema.sql             # Database schema (if using PostgreSQL)
│
└── .env.example               # Environment variables template
```

---

## 🧪 Testing the Application

### Test Endpoint 1: Analyze All Data
```bash
curl http://localhost:8000/analysis/
```

### Test Endpoint 2: Analyze Specific SME
```bash
curl "http://localhost:8000/analysis/?business_id=SME_1&show_raw=true"
```

### Test Endpoint 3: Get SME List
```bash
curl http://localhost:8000/analysis/smes
```

### Test Endpoint 4: Health Check
```bash
curl http://localhost:8000/health
```

---

## 🎨 Features Explained

### Financial Metrics

| Metric | Description |
|--------|-------------|
| **Annual Revenue** | Total revenue for the period |
| **Total Expenses** | Sum of all operational costs |
| **Profit** | Revenue minus expenses |
| **Profit Margin** | Profit as percentage of revenue |
| **Cash Health Ratio** | Measure of liquidity and cash availability |
| **Debt-Equity Ratio** | Financial leverage indicator |
| **Financial Health Score** | Composite score (0-100) |
| **Risk Level** | High/Medium/Low categorization |

### AI Recommendations

The system generates smart, actionable recommendations based on:
- **High Risk**: Cost reduction, emergency financing, restructuring advice
- **Medium Risk**: Working capital optimization, cost control strategies
- **Low Risk**: Growth opportunities, expansion strategies, investment guidance

### Risk Categories
- 🔴 **High Risk**: Negative profit or low cash ratio
- 🟡 **Medium Risk**: Expenses > 85% of revenue or cash ratio < 1.5
- 🟢 **Low Risk**: Healthy financials with growth potential

---

## 🔧 Configuration & Customization

### Environment Variables
See `.env.example` for all available configuration options.

### Modifying AI Recommendations
Edit `backend/ai_engine.py` to adjust recommendation logic based on metrics.

### Updating Financial Metrics
Edit `backend/financial_analysis.py` to add custom metric calculations.

### Styling
Modify `frontend/src/components/Dashboard.css` for UI customization.

---

## 🐛 Troubleshooting

### Issue: Backend fails to start
```
Solution: Ensure Python 3.9+ is installed and venv is activated
pip install -r requirements.txt --upgrade
```

### Issue: Frontend can't connect to backend
```
Solution: Check backend is running on port 8000
Verify CORS is enabled in main.py
Check browser console for errors
```

### Issue: CSV not found
```
Solution: Ensure sample_data/SME_Financial_Health_Dataset.csv exists
Check file path in backend/routes/analysis.py (DATA_PATH)
```

### Issue: Port already in use
```
Backend: python -m uvicorn main:app --port 8001
Frontend: PORT=3001 npm start
```

---

## 📝 Sample Data Format

The CSV should contain these columns:
```
business_id,industry_type,annual_revenue,total_expenses,
loan_amount,emi_amount,gst_compliance_status,current_ratio,
quick_ratio,debt_equity_ratio,dscr,roce,
financial_health_score,risk_category,ai_recommendation
```

---

## 🚀 Deployment

### Production Build

**Frontend:**
```bash
cd frontend
npm run build
# Creates optimized build in frontend/build/
```

**Backend:**
```bash
# Use Gunicorn for production
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 main:app
```

### Docker (Optional)
Create `Dockerfile` for containerized deployment.

---

## 📚 API Documentation

Once backend is running, visit:
```
Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc
```

---

## 🤝 Contributing

To extend the platform:

1. **Add new metrics**: Modify `financial_analysis.py`
2. **New recommendations**: Update `ai_engine.py`
3. **New endpoints**: Add routes in `routes/analysis.py`
4. **UI components**: Create in `frontend/src/components/`

---

## 📄 License

This project is part of the Financial Health Assessment Challenge.

---

## ✨ Key Improvements Made

✅ Complete error handling and validation
✅ Enhanced financial metrics calculation
✅ Improved AI recommendations with risk-based logic
✅ Modern, responsive UI with professional styling
✅ Comprehensive API documentation
✅ Health check and status endpoints
✅ Environment configuration support
✅ Better logging and debugging

---

## 🎯 Next Steps

1. ✅ Install dependencies
2. ✅ Configure environment variables
3. ✅ Start backend server
4. ✅ Start frontend application
5. ✅ Open browser and analyze SME data
6. ✅ Review AI recommendations
7. ✅ Export results as JSON/PDF

---

## 📞 Support

For issues or questions:
1. Check browser console for errors
2. Review backend logs in terminal
3. Verify all ports are accessible
4. Ensure CSV data format is correct
5. Check API documentation at `/docs`

---

**Built with ❤️ for SME Financial Health**

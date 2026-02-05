# Testing Guide - SME Financial Health Assessment Platform

## 🧪 Complete Testing Checklist

### Prerequisites
- Backend running on http://localhost:8000
- Frontend running on http://localhost:3000
- Sample data CSV exists in `backend/sample_data/SME_Financial_Health_Dataset.csv`

---

## ✅ Backend Tests

### 1. Health Check
```bash
curl http://localhost:8000/health
```

**Expected Response:**
```json
{
  "status": "healthy",
  "timestamp": "2026-02-03T10:30:00"
}
```

### 2. Root Endpoint
```bash
curl http://localhost:8000/
```

**Expected Response:**
```json
{
  "status": "online",
  "service": "SME Financial Health Assessment Platform",
  "version": "1.0.0",
  "timestamp": "2026-02-03T10:30:00"
}
```

### 3. Get All SMEs Analysis
```bash
curl http://localhost:8000/analysis/
```

**Expected:**
- Returns metrics for all SMEs in dataset
- Contains rows, columns, metrics, ai_recommendations

### 4. Analyze Specific SME (SME_1)
```bash
curl "http://localhost:8000/analysis/?business_id=SME_1"
```

**Expected Response:**
```json
{
  "rows": 1,
  "columns": ["business_id", "industry_type", "annual_revenue", ...],
  "metrics": {
    "annual_revenue": 34999221,
    "total_expenses": 26355176,
    "profit": 8644045,
    "profit_margin": 24.7,
    "cash_health_ratio": 2.63,
    "risk_level": "Low Risk",
    "financial_health_score": 100,
    "debt_equity_ratio": 2.4,
    "dscr": 2.61,
    "roce": 24.03
  },
  "ai_recommendations": [
    "✓ Maintain current financial discipline...",
    "🎯 Excellent position: Eligible for growth investment...",
    ...
  ],
  "raw": null
}
```

### 5. Analyze SME with Raw Data
```bash
curl "http://localhost:8000/analysis/?business_id=SME_1&show_raw=true"
```

**Expected:**
- Same as above, plus full row data in "raw" field

### 6. List Available SMEs
```bash
curl http://localhost:8000/analysis/smes
```

**Expected Response:**
```json
{
  "smes": ["SME_1", "SME_2", "SME_3", "SME_4", ...]
}
```

### 7. Test Invalid SME ID
```bash
curl "http://localhost:8000/analysis/?business_id=INVALID_123"
```

**Expected:**
- HTTP 404 error
- Error message: "SME not found"

### 8. API Documentation
Open in browser: `http://localhost:8000/docs`

**Expected:**
- Interactive Swagger UI showing all endpoints
- Test endpoints directly from browser

---

## 🖥️ Frontend Tests

### 1. Page Loads Correctly
- Navigate to http://localhost:3000
- Page should load without errors
- Header should show "Financial Health — SME Analyzer"

### 2. Initial Data Load
- Dashboard automatically loads all SME data
- Shows total rows and columns count
- API status shows "✓ API online"

### 3. Search Specific SME
1. Type "SME_1" in the search box
2. Click "Analyze" button
3. Should show financial metrics for SME_1
4. Risk badge should display

### 4. Display Financial Metrics
- Verify all metrics display correctly:
  - Annual Revenue
  - Total Expenses
  - Profit
  - Profit Margin
  - Cash Health Ratio
  - Risk Level
  - Financial Health Score
  - Debt-Equity Ratio

### 5. AI Recommendations
- At least 3-4 recommendations should display
- Each recommendation should be actionable
- Format: "✓ " for positive, "⚠️ " for urgent, "🎯 " for opportunities

### 6. Show Raw Data
1. Check "Show raw data" checkbox
2. Click Analyze
3. Raw data section should appear with all fields

### 7. Export JSON
1. Analyze an SME
2. Click "📥 Export JSON" button
3. Browser should download a JSON file

### 8. Print/Export
1. Click "🖨️ Print" button
2. Browser print dialog should open
3. Should show metrics and recommendations

### 9. Error Handling
1. Disconnect backend (stop server)
2. Try to analyze
3. Should show error message
4. API status should change to "✗ API offline"

### 10. Responsive Design
1. Open browser DevTools (F12)
2. Test on different screen sizes:
   - Desktop (1920x1080)
   - Tablet (768x1024)
   - Mobile (375x667)
3. Layout should adapt properly

---

## 📊 Data Validation Tests

### Test Dataset (SME_1)
```
business_id: SME_1
industry_type: E-commerce
annual_revenue: 34,999,221
total_expenses: 26,355,176
profit: 8,644,045
current_ratio: 2.63
debt_equity_ratio: 2.4
financial_health_score: 100
risk_category: Low Risk
```

### Risk Level Tests

#### Test High Risk SME (SME_2)
```bash
curl "http://localhost:8000/analysis/?business_id=SME_2"
```

Should have:
- Risk Level: "High Risk" or "Medium Risk"
- Lower financial health score
- Different recommendations

#### Test Low Risk SME (SME_1)
```bash
curl "http://localhost:8000/analysis/?business_id=SME_1"
```

Should have:
- Risk Level: "Low Risk"
- High financial health score (>80)
- Growth-focused recommendations

---

## 🔍 Edge Case Tests

### 1. Empty Business ID
```bash
curl "http://localhost:8000/analysis/?business_id="
```

**Expected:** Should treat as no filter

### 2. Case Insensitive Search
```bash
curl "http://localhost:8000/analysis/?business_id=sme_1"
```

**Expected:** Should find SME_1 (case-insensitive)

### 3. Special Characters in ID
```bash
curl "http://localhost:8000/analysis/?business_id=SME-1"
```

**Expected:** Should find SME_1 (hyphen/underscore treated as equivalent)

### 4. No Data Available
- If CSV is empty, should return error 400
- If CSV is missing, should return error 404

### 5. Malformed CSV
- If CSV has wrong format, should handle gracefully
- Should not crash the backend

---

## 📈 Performance Tests

### Load Test - Analyze All SMEs
```bash
time curl http://localhost:8000/analysis/
```

**Expected:**
- Response time < 1 second for ~4-5 SMEs
- No memory leaks
- Consistent performance

### Concurrent Requests
```bash
for i in {1..5}; do
  curl "http://localhost:8000/analysis/?business_id=SME_1" &
done
```

**Expected:**
- All requests complete successfully
- No race conditions
- Proper error handling

---

## 🐛 Error Handling Tests

### 1. Database Connection Error
If using PostgreSQL:
```bash
# Stop PostgreSQL service
# Try to analyze
```

**Expected:**
- Graceful error message
- Backend still responsive
- User sees helpful error

### 2. Missing CSV File
```bash
# Rename sample_data/SME_Financial_Health_Dataset.csv
curl http://localhost:8000/analysis/
```

**Expected:**
- HTTP 404 error
- Message: "Dataset not found"

### 3. Invalid JSON Response
Modify a response to return invalid JSON
**Expected:**
- Frontend shows error message
- No JavaScript console errors

### 4. Timeout Test
```bash
# Make very slow query or
# Set artificially low timeout
```

**Expected:**
- Request times out gracefully
- User gets error message

---

## ✨ Feature Tests

### 1. Metric Calculations
For SME_1:
- Revenue: 34,999,221
- Expenses: 26,355,176
- Expected Profit: 8,644,045
- Expected Profit Margin: 24.7%

Verify calculations are correct.

### 2. Risk Level Logic
- **High Risk**: profit < 0 OR cash_ratio < 0.5
- **Medium Risk**: expense_ratio > 0.85 OR cash_ratio < 1.0
- **Low Risk**: Everything else

Test each scenario.

### 3. Financial Health Score
- Score from 0-100
- Visual progress bar
- Color coding (green for high, red for low)

### 4. AI Recommendations
- At least 3 recommendations
- Different for each risk level
- Actionable and specific
- Include emoji indicators

---

## 📝 Manual Acceptance Tests

### Scenario 1: E-commerce SME (SME_1)
1. Open http://localhost:3000
2. Enter "SME_1"
3. Click Analyze
4. Verify:
   - Shows revenue, expenses, profit
   - Risk: Low Risk
   - Score: 100
   - Recommendations include growth opportunities

### Scenario 2: Logistics with Issues (SME_2)
1. Enter "SME_2"
2. Click Analyze
3. Verify:
   - Lower score
   - Higher risk level
   - Recommendations focus on cost control

### Scenario 3: Manufacturing (SME_3)
1. Enter "SME_3"
2. Click Analyze
3. Verify:
   - Industry-appropriate metrics
   - Consistent calculations
   - Clear recommendations

---

## 🔒 Security Tests

### 1. CORS Headers
```bash
curl -i -X OPTIONS http://localhost:8000/analysis/ \
  -H "Origin: http://localhost:3000"
```

**Expected:**
- `Access-Control-Allow-Origin: *`
- `Access-Control-Allow-Methods: *`

### 2. Input Validation
```bash
curl "http://localhost:8000/analysis/?business_id=<script>alert('xss')</script>"
```

**Expected:**
- Should be escaped/sanitized
- No code execution
- Safe error response

### 3. Large File Upload
- Should handle large CSV files
- Timeout if too large (>50MB)
- Graceful error message

---

## ✅ Final Verification Checklist

- [ ] Backend starts without errors
- [ ] Frontend loads correctly
- [ ] All 6+ API endpoints responding
- [ ] Financial metrics calculate correctly
- [ ] AI recommendations generate
- [ ] Risk levels assigned correctly
- [ ] Error handling works properly
- [ ] Responsive design functions
- [ ] Export/Print features work
- [ ] API documentation loads
- [ ] No console errors
- [ ] Performance acceptable
- [ ] Security measures in place
- [ ] Data properly displayed
- [ ] UI is professional and clean

---

## 🎯 Test Execution Order

1. **Backend Startup** → Verify health check
2. **API Endpoints** → Test all endpoints individually
3. **Frontend Load** → Verify page loads
4. **Data Display** → Verify correct data shown
5. **User Interactions** → Test clicks and inputs
6. **Edge Cases** → Test error scenarios
7. **Performance** → Check response times
8. **Security** → Verify protections
9. **Responsive** → Test different screen sizes
10. **Final Polish** → Verify UI/UX quality

---

## 📊 Test Results Template

```
Date: 2026-02-03
Backend: ✅ Running
Frontend: ✅ Running
API Health: ✅ Healthy

Endpoints Tested:
- GET / ✅
- GET /health ✅
- GET /analysis/ ✅
- GET /analysis/?business_id=SME_1 ✅
- GET /analysis/smes ✅

Frontend Tests:
- Page Load ✅
- Data Display ✅
- Search ✅
- Metrics ✅
- Recommendations ✅
- Export ✅

Issues Found: None
```

---

**All tests passing = Ready for production! 🚀**

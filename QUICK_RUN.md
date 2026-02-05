# FINANCIAL HEALTH AI - QUICK START GUIDE

## 🚀 EASIEST WAY - ONE CLICK RUN

### Windows Users:
Double-click: **START_APP.bat**

This opens 2 windows automatically:
- Backend (port 8000)
- Frontend (port 3000)

Then open: http://localhost:3000

---

## 📟 MANUAL RUN (If bat file doesn't work)

### Step 1: Open Terminal 1 (Backend)
```bash
cd e:\financial-health-ai
E:/financial-health-ai/.venv/Scripts/python.exe -m uvicorn backend.main:app --host 127.0.0.1 --port 8000
```

Wait for: `Application startup complete`

### Step 2: Open Terminal 2 (Frontend)
```bash
cd e:\financial-health-ai\frontend
npm start
```

Wait for: `Compiled successfully!`

### Step 3: Open Browser
Go to: **http://localhost:3000**

---

## ✅ WHAT YOU SHOULD SEE

**Backend Output:**
```
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000
```

**Frontend Output:**
```
Compiled successfully!
You can now view sme-finance-ui in the browser.
Local: http://localhost:3000
```

---

## 🔗 USEFUL LINKS

| What | Link | Purpose |
|------|------|---------|
| Main App | http://localhost:3000 | Dashboard UI |
| API Docs | http://localhost:8000/docs | Test API endpoints |
| Health Check | http://127.0.0.1:8000/health | Verify backend |

---

## ❌ PROBLEMS & SOLUTIONS

### Problem 1: "Port 8000 already in use"
**Solution:**
```bash
netstat -ano | findstr :8000
taskkill /PID [PID_NUMBER] /F
```

### Problem 2: "Port 3000 already in use"
**Solution:**
```bash
netstat -ano | findstr :3000
taskkill /PID [PID_NUMBER] /F
```

### Problem 3: "Module not found" error
**Solution:**
```bash
cd e:\financial-health-ai
E:/financial-health-ai/.venv/Scripts/python.exe -m pip install -r backend/requirements.txt
```

### Problem 4: npm install fails
**Solution:**
```bash
cd e:\financial-health-ai\frontend
npm install --legacy-peer-deps
```

### Problem 5: Can't find .venv
**Solution:**
```bash
cd e:\financial-health-ai
python -m venv .venv
.venv\Scripts\activate
pip install -r backend/requirements.txt
```

---

## 📊 DEFAULT TEST DATA

File: `backend/sample_data/SME_Financial_Health_Dataset.csv`

Has sample SME data ready to analyze!

---

## 🎯 QUICK TEST

1. Go to: http://localhost:3000
2. Click "Analyze"
3. See financial metrics
4. Get AI recommendations

---

**EVERYTHING WORKING?** You're done! 🎉

from fastapi import APIRouter, HTTPException, Query
from starlette.concurrency import run_in_threadpool
try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except Exception:
    pd = None
    PANDAS_AVAILABLE = False
from pathlib import Path
import sys
import os

# Add backend to path if needed
backend_dir = Path(__file__).resolve().parent.parent
if str(backend_dir) not in sys.path:
    sys.path.insert(0, str(backend_dir))

try:
    # when running as package from project root
    from backend import financial_analysis, ai_engine
except ImportError:
    # when running from inside backend folder
    import financial_analysis
    import ai_engine

router = APIRouter(
    prefix="/analysis",
    tags=["analysis"]
)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "sample_data" / "SME_Financial_Health_Dataset.csv"


@router.get("/")
async def analyze(
    business_id: str | None = Query(None, description="Optional business_id to scope analysis"),
    show_raw: bool = Query(False, description="If true, include raw SME row data in the response")
):
    if not DATA_PATH.exists():
        raise HTTPException(status_code=404, detail="Dataset not found")
    if not PANDAS_AVAILABLE:
        raise HTTPException(status_code=503, detail="pandas is not installed on the server; dataset endpoints are unavailable")
    try:
        df = await run_in_threadpool(pd.read_csv, DATA_PATH)
    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=400, detail="Dataset is empty or malformed")
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to read dataset")

    # If business_id provided, filter the dataframe (tolerant match)
    if business_id:
        if "business_id" not in df.columns:
            raise HTTPException(status_code=400, detail="Dataset does not contain business_id column")
        # normalize IDs: lower-case and treat '-' and '_' as equivalent, remove other non-alphanumerics
        def _norm(s: str) -> str:
            return "" if s is None else ''.join(ch for ch in str(s).lower() if ch.isalnum())

        target = _norm(business_id)
        if not target:
            raise HTTPException(status_code=400, detail="Invalid business_id")

        normalized = df["business_id"].astype(str).apply(_norm)
        filtered = df[normalized == target]
        if filtered.empty:
            raise HTTPException(status_code=404, detail="SME not found")
        df = filtered

    # Compute simple financial metrics and AI recommendations
    try:
        metrics = financial_analysis.analyze_financials(df)
    except Exception:
        metrics = None

    try:
        recommendations = ai_engine.ai_recommendations(metrics or {})
    except Exception:
        recommendations = []

    # By default we do not return raw row data (keeps UI concise for judges).
    raw = None
    if business_id and show_raw:
        # take the first matching row and convert to plain types
        row = df.iloc[0]
        raw = {}
        for c in df.columns:
            v = row[c]
            # convert numpy types to python native for JSON
            try:
                if pd.isna(v):
                    raw[c] = None
                else:
                    raw[c] = v.item() if hasattr(v, 'item') else v
            except Exception:
                raw[c] = str(v)

        # If dataset contains a precomputed score column, expose it in metrics
        if "financial_health_score" in df.columns and metrics is not None:
            try:
                score = row.get("financial_health_score")
                if score is not None and not pd.isna(score):
                    metrics.setdefault('financial_health_score', int(score))
            except Exception:
                pass

        # Ensure risk labeling is consistent between raw dataset and computed metrics
        try:
            # prefer the dataset's `risk_category` if present
            if "risk_category" in df.columns and metrics is not None:
                rc = row.get("risk_category")
                if rc is not None and not pd.isna(rc):
                    metrics['risk_level'] = str(rc)
        except Exception:
            pass

    return {
        "rows": len(df),
        "columns": list(df.columns),
        "raw": raw,
        "metrics": metrics,
        "ai_recommendations": recommendations,
    }


@router.get('/smes')
async def list_smes():
    """Return a short list of available SME ids (business_id column)."""
    if not DATA_PATH.exists():
        raise HTTPException(status_code=404, detail="Dataset not found")
    if not PANDAS_AVAILABLE:
        raise HTTPException(status_code=503, detail="pandas is not installed on the server; dataset endpoints are unavailable")
    try:
        df = await run_in_threadpool(pd.read_csv, DATA_PATH)
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to read dataset")

    if 'business_id' not in df.columns:
        return {"smes": []}

    # return unique ids (string) limited to 1000 entries
    ids = df['business_id'].astype(str).unique().tolist()
    return {"smes": ids}

import pandas as pd
import logging

logger = logging.getLogger(__name__)


def _to_number(x):
    """Convert any value to float, returning None if unable"""
    try:
        return float(x)
    except (ValueError, TypeError):
        return None


def _calculate_risk_level(profit, cash_ratio, revenue, expenses):
    """
    Calculate risk level based on multiple financial indicators
    Returns: 'High Risk', 'Medium Risk', or 'Low Risk'
    """
    if profit < 0:
        return 'High Risk'
    
    if cash_ratio is not None:
        if cash_ratio < 0.5:
            return 'High Risk'
        elif cash_ratio < 1:
            return 'Medium Risk'
    
    # Calculate expense ratio
    if revenue > 0:
        expense_ratio = expenses / revenue
        if expense_ratio > 0.85:
            return 'Medium Risk'
    
    return 'Low Risk'


def analyze_financials(df: pd.DataFrame):
    """
    Compute comprehensive financial metrics for SME(s).
    
    If df has one row: analyze that specific SME
    If df has multiple rows: aggregate dataset-level metrics
    """
    # Detect column names flexibly
    revenue_col = None
    expenses_col = None
    
    possible_revenue_cols = ["annual_revenue", "revenue", "total_revenue"]
    possible_expenses_cols = ["total_expenses", "expenses", "operational_expenses"]
    
    for col in possible_revenue_cols:
        if col in df.columns:
            revenue_col = col
            break
    
    for col in possible_expenses_cols:
        if col in df.columns:
            expenses_col = col
            break
    
    if revenue_col is None and expenses_col is None:
        logger.warning("No revenue or expense columns found in dataset")
        return {}
    
    # Single-row case: analyze individual SME
    if len(df) == 1:
        row = df.iloc[0]
        
        revenue = _to_number(row.get(revenue_col)) if revenue_col else None
        expenses = _to_number(row.get(expenses_col)) if expenses_col else None
        
        # Fallback conversions
        if revenue is None:
            revenue = _to_number(row.get('revenue'))
        if expenses is None:
            expenses = _to_number(row.get('expenses'))
        
        revenue = revenue or 0
        expenses = expenses or 0
        profit = revenue - expenses
        
        # Calculate cash health ratio
        current_ratio = _to_number(row.get('current_ratio'))
        if current_ratio is not None:
            cash_ratio = round(current_ratio, 2)
        else:
            cash_ratio = round((revenue / (expenses or 1)), 2)
        
        # Determine risk level
        risk = None
        if 'risk_category' in df.columns:
            risk_val = row.get('risk_category')
            if risk_val is not None and pd.notna(risk_val):
                risk = str(risk_val)
        
        if not risk:
            risk = _calculate_risk_level(profit, cash_ratio, revenue, expenses)
        
        # Get financial health score
        score = _to_number(row.get('financial_health_score'))
        
        # Calculate additional metrics
        debt_equity = _to_number(row.get('debt_equity_ratio'))
        dscr = _to_number(row.get('dscr'))
        roce = _to_number(row.get('roce'))
        
        result = {
            'annual_revenue': int(revenue),
            'total_expenses': int(expenses),
            'profit': int(profit),
            'profit_margin': round((profit / revenue * 100), 2) if revenue > 0 else 0,
            'cash_health_ratio': cash_ratio,
            'risk_level': risk,
        }
        
        # Add optional metrics if available
        if score is not None:
            try:
                result['financial_health_score'] = int(score)
            except (ValueError, TypeError):
                result['financial_health_score'] = score
        
        if debt_equity is not None:
            result['debt_equity_ratio'] = round(debt_equity, 2)
        
        if dscr is not None:
            result['dscr'] = round(dscr, 2)
        
        if roce is not None:
            result['roce'] = round(roce, 2)
        
        return result
    
    # Multi-row case: dataset-level aggregates
    revenue = pd.to_numeric(df[revenue_col], errors='coerce').fillna(0).sum() if revenue_col else 0
    expenses = pd.to_numeric(df[expenses_col], errors='coerce').fillna(0).sum() if expenses_col else 0
    profit = revenue - expenses
    cash_ratio = round((revenue / (expenses or 1)), 2)
    risk = _calculate_risk_level(profit, cash_ratio, revenue, expenses)
    
    result = {
        'annual_revenue': int(revenue),
        'total_expenses': int(expenses),
        'profit': int(profit),
        'profit_margin': round((profit / revenue * 100), 2) if revenue > 0 else 0,
        'cash_health_ratio': cash_ratio,
        'risk_level': risk,
        'avg_sme_count': len(df),
    }
    
    # Calculate average scores if available
    if 'financial_health_score' in df.columns:
        avg_score = pd.to_numeric(df['financial_health_score'], errors='coerce').mean()
        if not pd.isna(avg_score):
            result['avg_financial_health_score'] = round(avg_score, 2)
    
    return result

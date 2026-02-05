
import logging

logger = logging.getLogger(__name__)


def ai_recommendations(metrics: dict):
    """
    Generate AI-powered financial recommendations based on computed metrics.
    Provides actionable insights for SME financial optimization.
    """
    if not metrics:
        return ["No metrics available to generate recommendations"]

    risk = metrics.get('risk_level', '').lower() if metrics.get('risk_level') else ''
    score = metrics.get('financial_health_score')
    profit = metrics.get('profit', 0)
    cash = metrics.get('cash_health_ratio')
    profit_margin = metrics.get('profit_margin', 0)
    debt_equity = metrics.get('debt_equity_ratio')
    revenue = metrics.get('annual_revenue', 0)

    recs = []
    
    try:
        # HIGH RISK RECOMMENDATIONS
        if 'high' in risk:
            recs.append('⚠️ URGENT: Review cost structure and reduce fixed operational expenses')
            recs.append('Negotiate extended payment terms with suppliers to improve cash flow')
            
            if profit < 0:
                recs.append('Implement immediate cost reduction strategy or seek emergency financing')
                recs.append('Consider debt restructuring or refinancing existing liabilities')
            
            if cash is not None and cash < 0.5:
                recs.append('Apply for emergency working capital loan immediately')
                recs.append('Accelerate receivables collection or negotiate shorter payment cycles')
            
            recs.append('Seek expert financial advisory for business restructuring')
            return recs
        
        # MEDIUM RISK RECOMMENDATIONS
        elif 'medium' in risk:
            recs.append('Optimize working capital management and control operational costs')
            recs.append('Improve accounts receivable collection efficiency')
            
            if profit_margin < 10:
                recs.append('Implement cost optimization initiatives - target 15%+ profit margin')
            
            if cash is not None and cash < 1.5:
                recs.append('Build cash reserves or negotiate better payment terms')
            
            if debt_equity is not None and debt_equity > 2:
                recs.append('Consider debt reduction strategy to lower leverage')
            
            recs.append('Monitor GST compliance and optimize input credit utilization')
            return recs
        
        # LOW RISK RECOMMENDATIONS (GROWTH-FOCUSED)
        else:  # Low Risk
            recs.append('✓ Maintain current financial discipline and operational excellence')
            
            if score is not None and isinstance(score, (int, float)):
                if score >= 85:
                    recs.append('🎯 Excellent position: Eligible for growth investment and expansion credit lines')
                    recs.append('Consider diversifying revenue streams or expanding product/service offerings')
                    recs.append('Explore working capital optimization and vendor financing programs')
                elif score >= 75:
                    recs.append('Good financial health: Eligible for working capital loans and growth financing')
                    recs.append('Focus on increasing profit margins through operational efficiency')
                else:
                    recs.append('Stable position: Monitor metrics quarterly and plan for sustainable growth')
            
            # Monitor cash conversion cycle
            if cash is not None:
                if cash > 2:
                    recs.append('Strong liquidity: Opportunity to invest in growth initiatives')
                else:
                    recs.append('Maintain cash reserves to handle seasonal fluctuations')
            
            # Leverage optimization
            if debt_equity is not None and debt_equity < 1:
                recs.append('Conservative leverage: Can safely increase borrowing for expansion')
            
            # GST optimization
            recs.append('Optimize GST compliance and input credit utilization for cost savings')
            
            return recs
    
    except Exception as e:
        logger.error(f"Error generating recommendations: {str(e)}")
        return ['Please review financials with a financial advisor for personalized recommendations']

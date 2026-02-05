try:
    from backend.routes import analysis
except ModuleNotFoundError:
    # Allow running this script directly from the backend/ directory
    from routes import analysis
import pandas as pd

print('DATA_PATH ->', analysis.DATA_PATH)
try:
    df = pd.read_csv(analysis.DATA_PATH)
    print({'rows': len(df), 'columns': list(df.columns)})
except Exception as e:
    print('error reading csv:', e)

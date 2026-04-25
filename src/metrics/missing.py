
def check_missing(df):
    missing_percentage = df.isnull().mean()
    
    result = {}
    for col, val in missing_percentage.items():
        result[col] = round(val, 3)
    
    return result

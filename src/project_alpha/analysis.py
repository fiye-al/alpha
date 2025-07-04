def analyze(df):
    summary = {
        'rows': len(df),
        'columns': list(df.columns)
    }
    print("Analysis summary:", summary)
    return summary

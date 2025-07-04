import pandas as pd

def process_data(path):
    df = pd.read_csv(path)
    print(f"Processed {len(df)} records")
    return df

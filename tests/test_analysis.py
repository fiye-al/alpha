from project_alpha.analysis import analyze
import pandas as pd

def test_analyze():
    df = pd.DataFrame({'a':[1,2,3]})
    summary = analyze(df)
    assert summary['rows'] == 3
    assert 'a' in summary['columns']

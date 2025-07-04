import pandas as pd
import pytest
from project_alpha.analysis import analyze

def test_analyze_basic(capsys):
    # Basic single-column DataFrame
    df = pd.DataFrame({'col1': [10, 20, 30]})
    summary = analyze(df)
    # Capture and verify printed output
    captured = capsys.readouterr()
    assert "Analysis summary" in captured.out
    # Verify summary contents
    assert summary['rows'] == 3
    assert summary['columns'] == ['col1']

def test_analyze_multiple_columns(capsys):
    # Multi-column DataFrame
    data = {
        'a': [1, 2, 3, 4],
        'b': ['x', 'y', 'z', 'w'],
        'c': [True, False, True, False]
    }
    df = pd.DataFrame(data)
    summary = analyze(df)
    captured = capsys.readouterr()
    assert "Analysis summary" in captured.out
    assert summary['rows'] == 4
    # Column order should match insertion order
    assert summary['columns'] == ['a', 'b', 'c']

def test_analyze_empty_dataframe(capsys):
    # Empty DataFrame with no rows but defined columns
    df = pd.DataFrame(columns=['foo', 'bar'])
    summary = analyze(df)
    captured = capsys.readouterr()
    assert "Analysis summary" in captured.out
    assert summary['rows'] == 0
    assert summary['columns'] == ['foo', 'bar']

def test_analyze_no_columns(capsys):
    # DataFrame with no columns at all
    df = pd.DataFrame()
    summary = analyze(df)
    captured = capsys.readouterr()
    assert "Analysis summary" in captured.out
    assert summary['rows'] == 0
    assert summary['columns'] == []

def test_analyze_non_dataframe_input():
    # Passing something that isn't a DataFrame should raise an attribute error
    with pytest.raises(AttributeError):
        analyze("not a dataframe")

def test_analyze_large_dataframe(capsys):
    # Large DataFrame performance smoke test
    df = pd.DataFrame({'x': range(1000), 'y': range(1000, 2000)})
    summary = analyze(df)
    captured = capsys.readouterr()
    assert summary['rows'] == 1000
    assert summary['columns'] == ['x', 'y']

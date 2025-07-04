from project_alpha.data_processing import process_data
from pathlib import Path

def test_process(tmp_path):
    p = tmp_path / "test.csv"
    p.write_text("id,value
1,5
2,10
")
    df = process_data(str(p))
    assert df.shape == (2,2)

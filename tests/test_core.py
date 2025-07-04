import pytest
from project_alpha.core import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Project Alpha core running" in captured.out

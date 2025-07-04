from project_alpha.utils import helper, another_util

def test_helper():
    assert helper() == "Helper function"

def test_another_util():
    assert another_util(2, 3) == 5

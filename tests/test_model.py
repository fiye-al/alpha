from project_alpha.models.model import train_model

def test_train():
    clf = train_model()
    assert hasattr(clf, 'fit')

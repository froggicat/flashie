from app import app


def test_home_returns_200():
    # Flask's test client pretends to be a browser — no flask run needed
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert "Spec Companion" in response.get_data(as_text=True)

def test_coverage():
    client = app.test_client()
    response = client.get("/coverage")
    assert response.status_code == 200
    assert "Coverage" in response.get_data(as_text=True)

def test_study_spec_point_16():
    client = app.test_client()
    response = client.get("/study?spec_point=16")
    assert response.status_code == 200
    assert "Studying" in response.get_data(as_text=True)

def test_spec_16():
    client = app.test_client()
    response = client.get("/spec/16")
    assert response.status_code == 200
    assert "Electricity" in response.get_data(as_text=True)
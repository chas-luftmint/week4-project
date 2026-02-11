from app import app


def test_main_page():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Main Page' in response.data


def test_working_page():
    client = app.test_client()
    response = client.get('/working')
    assert response.status_code == 200
    assert b'This works' in response.data
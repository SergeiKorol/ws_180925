import requests

def test_add():

    body = {"title": "test", "completed": True}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)

    assert response.status_code == 400


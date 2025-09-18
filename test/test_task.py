import requests


def test_to_do():
    body = {"title": "Создать задачу", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    to_id = response.json()["id"]

    body = {"title": "Изменить задачу"}
    response = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    after_id = response.json()["id"]
    assert response.status_code == 200
    assert to_id == after_id



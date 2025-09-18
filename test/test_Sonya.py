import requests

def test_task_Sonya():
    """
    Создает задачу.
    Удаляет по id.
    Проверка удаления.
    :return:
    """
    body = {"title": "task_Sonya", "completed": False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = response.json()["id"]
    requests.delete(f'https://todo-app-sky.herokuapp.com/{id}')
    response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')

    assert response.status_code == 404
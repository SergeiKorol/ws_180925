import requests
"""изменено название"""

def work_add():

    body = {"title": "work", "completed": True}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)

    assert response.status_code == 400


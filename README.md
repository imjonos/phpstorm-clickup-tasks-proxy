# ClickUp integration with PhpStorm Alpha 0.0.1
Simple proxy app for using ClickUp as a tasks server in the PHPSTORM and other IDEs.

My first python app)
# Run
- copy .env.example to .env
- pip install pyclickup
- pip install flask
- python3.9 main.py
# Configuration PHPSTORM 
![image](https://user-images.githubusercontent.com/5132976/155839213-6d3e5a55-cc7b-4f2d-af8a-5c460b658d68.png)

- New Generic Server 
- tasksListUrl: {serverUrl}/api/v1/tasks
- Response type: JSON
- tasks: *
- id: id
- summary: name
- description: description

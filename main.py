from pyclickup import ClickUp
import os
from dotenv import load_dotenv
from flask import Flask, json

api = Flask(__name__)


@api.route('/api/v1/tasks', methods=['GET'])
def get_companies():
    load_dotenv()
    api_key: str = os.getenv('API_KEY', '')
    team_id: int = int(os.getenv('TEAM', 0))
    space_id: int = int(os.getenv('SPACE', 0))
    project_id: int = int(os.getenv('PROJECT', 0))
    list_id: int = int(os.getenv('LIST', 0))
    statuses: list = json.loads(os.getenv('STATUSES', []))

    clickup = ClickUp(api_key)
    main_team = clickup.teams[team_id]
    main_space = main_team.spaces[space_id]
    main_project = main_space.projects[project_id]
    main_list = main_project.lists[list_id]
    tasks = main_list.get_all_tasks(include_closed=False, statuses=statuses)

    result: list = []

    for task in tasks:
        item = {
            'id': task.id,
            'name': task.name,
            'description': task.description,
            'url': task.url,
            'status': task.status.status
        }
        result.append(item)
    return json.dumps(result)


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=int(os.getenv('API_PORT', 8111)))

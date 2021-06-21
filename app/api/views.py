from flask import jsonify, request

from . import api
from ..main.trello import get_board_cards
from ..main.good_day_mock import get_good_day_project_id, receive_tasks
from ..models import User


@api.route('/import/tasks/<int:user_id>', methods=['POST'])
def import_trello_task(user_id):
    data = request.json
    token = User.query.filter_by(user_id=user_id).first().token
    project_id = data['trelloProjectId']
    good_day_project_id = get_good_day_project_id()
    tasks = get_board_cards(project_id, token)
    if tasks:
        # TODO: Send tasks to good day
        # TODO: Retrieve the id of the task
        return jsonify({
            'Status': 'OK',
            'goodday': receive_tasks(tasks, good_day_project_id)
        })
    else:
        return jsonify({'Status': 'error'})

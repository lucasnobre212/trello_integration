import requests
import json

from config import Config


def get_board_cards(board_id):
    url = f"https://api.trello.com/1/boards/{board_id}/cards"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'key': Config.TRELLO_API_KEY,
        'token': Config.TRELLO_TOKEN
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )
    return response.json()

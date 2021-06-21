import requests

from config import Config, DevelopmentConfig


def get_board_cards(board_id: str, token: str):
    url = f"https://api.trello.com/1/boards/{board_id}/cards"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'key': Config.TRELLO_API_KEY,
        'token': token
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )
    return response.json()


def oauth_authorize_url(user_id: int):
    trello_key = Config.TRELLO_API_KEY
    base_url = (f'https://trello.com/1/authorize?'
                f'expiration=1day&name={user_id}&scope=read&response_type=token&key={trello_key}'
                f'&return_url={DevelopmentConfig.OAUTH_DEVELOPMENT_URI}/{user_id}'
                )
    return base_url


def is_token_valid(token: str):
    url = f"https://api.trello.com/1/tokens/{token}"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'key': Config.TRELLO_API_KEY,
        'token': token
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )
    if response.status_code != 200:
        return False
    else:
        return True

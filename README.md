# Trello Integration API

## GET /oauth/authorize/<user_id>

    Check if user_id has a valid Trello's token in the database. If it does and it is valid,
     return status: connected, if not, sends an url for the user to generate a token

     Parameters:
        user_id: int

     Example:
     https://470cb6e4be93.ngrok.io/api/v1/oauth/authorize/1

## POST /import/tasks/<user_id>
    Get cards from given board id (trelloProjectId)

    Payload:
        trelloProjectId: str

    Parameters:
        user_id: int

    Example:
        https://470cb6e4be93.ngrok.io/api/v1/import/tasks/1

## POST /import/projects/<user_id>
    Get boards from given boards ids (trelloProjectIds) and then get their cards

    Payload:
        trelloProjectIds: str

    Parameters:
        user_id: int

    Example:
        https://470cb6e4be93.ngrok.io/api/v1/oauth/authorize/1
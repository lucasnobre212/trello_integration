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


# Things I would change in the long run
    Separate the import tasks. /import/tasks/<user_id> should return an identifier, so the web app or Good Day core
     can make a separate request to retrieve the data later.
    Take a look at the oauth routes, I am not sure if the way I am retrieving the token is safe
    Change how I am saving the token, saving it as a string in the database might not be a good idea
    Separate the database to a different service
    Add validators when communicating with trello, to make sure we are sending and retrieving the correct information.
     this also avoid errors when sending data to GoodDay.
    Take a look at FastApi framework, it looks like it is better to create APIs with Python


# game-backend-test server

This is the server for the game programmer back end test.
You should not need to change anything here, but you will need to run this server.

## System Requirements
- Docker, including docker compose. See https://docs.docker.com/get-docker/

## How to run
```
docker-compose up --force-recreate --build
```

## How to access
When server is running. Documentation can be found on 
```
http://127.0.0.1:8000/docs
```

### POST choices/{game}
Report a choice for `game`. Results are kept for 60 minutes.
Reports are on the form
```
{
    "playerId": str // unique identifier for the player
    "playerName": str // Display name of player
    "choice": int // selected value
}
```

### GET choices/{game}
Get all choices for `game` reported last 60 minutes.

```
{
    "choices": [
        {
            "playerId": str
            "playerName": str
            "choice": int
        },
        ...
    ]    
}
```
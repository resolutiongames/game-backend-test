import logging, os, json, redis
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional

url_prefix=''
app = FastAPI(docs_url=f'{url_prefix}/docs', redoc_url=f'{url_prefix}/redoc', openapi_url=f'{url_prefix}/openapi.json')

logging.basicConfig(level=logging.INFO)

@app.get('/')
def health_check():
    pass


class ChoiceRequest(BaseModel):
    playerName: str
    playerId: str
    choice: int

class ChoicesResponse():
    choices: List[ChoiceRequest]

@app.post('/choices/{game}')
async def report_a_choice(game:str, choice: ChoiceRequest):
    db = get_redis_connection()
    db.lpush(game,choice.json())
    db.expire(game, 60*60)

@app.get('/choices/{game}')
async def get_choices(game:str) -> ChoicesResponse:
    db = get_redis_connection()
    choices = []
    no_keys = db.llen(game)
    for i in range(0,no_keys):
        document = db.lindex(game,no_keys - i - 1)
        item = ChoiceRequest.parse_raw(document)
        choices.append(item)
    response = ChoicesResponse()
    response.choices = choices
    return response


redis_args = dict()
tournaments_db_name = 0

def get_redis_connection():
    redis_args = dict(
        host=os.getenv('REDIS_HOST'),
        port=os.getenv('REDIS_PORT'),
        health_check_interval=15
    )

    db_name = int(os.getenv('REDIS_DB'))

    return redis.Redis(**redis_args, db=db_name)

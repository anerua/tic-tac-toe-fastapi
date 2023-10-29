from typing import Union, List

from fastapi import FastAPI
from pydantic import BaseModel

from logic import play

app = FastAPI()


class GameState(BaseModel):
    state: List[str]
    maxi: str
    mini: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/play")
def make_play(game_state: GameState):
    play_response = play(game_state.state, game_state.mini, game_state.maxi)
    return {"state": play_response[0], "game_status": play_response[1]}

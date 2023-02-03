from typing import Union
from fastapi import FastAPI, Depends
from pydantic import BaseSettings
from functools import lru_cache


app = FastAPI()


class Settings(BaseSettings):
    ppp: str = "Sorry"
    
    class Config:
        env_file = ".kurno"


def get_settings():
    return Settings()


@app.get("/")
def read_root(settings: Settings = Depends(get_settings)):
    print(settings.ppp)
    return {"PPP": settings.ppp}

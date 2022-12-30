from fastapi import FastAPI

from schemas import AudioBook

app = FastAPI()


@app.get('/')
def home():
    return {"key": "Hello"}


@app.get('/{pk}')
def get_item(pk: int, string: float = None):
    return {"key": pk, "Welcome string": string}


@app.get('/user/{pk}/items/{item}')
def get_user_item(pk: int, item: str):
    return {"user": pk, "item": item}


@app.post('/book')
def create_audiobook(item: AudioBook):
    return item

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {"key": "Hello"}


@app.get('/{pk}')
def get_item(pk: int, string: float = None):
    return {"key": pk, "Welcome string": string}

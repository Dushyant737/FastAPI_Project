from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return "hello world !"

@app.get('/hello1')
def index():
    return "get the data"

@app.post('/hello2')
def index():
    return "post the data "    
from fastapi import FastAPI

myApp = FastAPI()

@myApp.get('/json_data')
def index():
    return {'message':'Hello World !'}
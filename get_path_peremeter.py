from fastapi import FastAPI

myApp = FastAPI()

"""
@myApp.get('/blog/all')
def get_all_blogs():
    return {'message':'all blogs provided !'}
"""    


@myApp.get('/blog/{id}')
def get_all_blogs(id:int):
    return {'message':f'My blog with blog_id {id} !'}    

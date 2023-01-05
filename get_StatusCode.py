from fastapi import FastAPI , status , Response

myApp = FastAPI()

"""
@myApp.get('/blog/{id}', status_code=404)
def get_blogs(id:int):
    if id > 5 :
        return {'error' : f'blog {id} not found'}
    else:
        return {'message':f'blog with id {id} !'}  
"""

"""
@myApp.get('/blog/{id}', status_code=status.HTTP_404_NOT_FOUND)
def get_blogs(id:int):
    if id > 5 :
        return {'error' : f'blog {id} not found'}
    else:
        return {'message':f'blog with id {id} !'}  
"""        
    


@myApp.get('/blog/{id}', status_code=status.HTTP_200_OK)
def get_blogs(id:int , response:Response):
    if id > 5 :
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error' : f'blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message':f'blog with id {id} !'}  
      
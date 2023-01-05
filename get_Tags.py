from fastapi import FastAPI , status , Response

myApp = FastAPI()

@myApp.get('/blog/all',tags=['Blog'])
def get_all_blogs():
    return {'message':'all blogs provided !'}


@myApp.get('/blog/all',tags=['VSF_Blog'])
def get_all_blogs():
    return {'message':'all blogs provided !'} 
     

@myApp.get('/blog/{id}', status_code=status.HTTP_200_OK , tags=['Default_Blog'])
def get_blogs(id:int , response:Response):
    if id > 5 :
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error' : f'blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message':f'blog with id {id} !'}  
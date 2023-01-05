from fastapi import FastAPI , status , Response

myApp = FastAPI()

"""
@myApp.get('/blog/all',
tags=['VSF_Blogs'],
summary='Retrive the all blogs data',
description='This API is fetching the all blogs',
response_description='This list all abount the blogs')
def get_all_blogs():
    return {'message':'all blogs provided !'}
"""

@myApp.get('/blog/all',tags=['Comments'])
def get_all_blogs():
    """
    Simulate retriving the blog
    - **id** mandatory path peremeter
    - **comment_id** mandatory path peremeter
    """    
    return {'message':'all blogs provided !'}     

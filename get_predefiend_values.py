from fastapi import FastAPI
from enum import Enum

myApp = FastAPI()

class BlogType(str , Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@myApp.get('/blog/type/{type}')
def get_all_blogs(type:BlogType):
    return {'message':f'blog type {type} !'} 
from fastapi import FastAPI
from enum import Enum
from typing import Optional

myApp = FastAPI()

# Query Parameters 
"""
@myApp.get('/blog/all')
def get_all_blogs(page, page_size):
    return {'message':f'all {page_size} belogs belongs to page {page} !'} 
"""

# Default values 

"""
@myApp.get('/blog/all')
def get_all_blogs(page =1, page_size = 10):
    return {'message':f'all {page_size} belogs belongs to page {page} !'}     
"""

# optinal query peremeters

"""
@myApp.get('/blog/all')
def get_all_blogs(page =1, page_size:Optional[int]=None):
    return {'message':f'all {page_size} blog belongs to page {page} !'}   
"""

# Cobmination of query and optinal


@myApp.get('/blog/{id}/comment_id/{comment_id}')
def get_comment(id : int, comment_id : int, valid:bool = True, username:Optional[str]=None):
    return {'message':f' blog_id {id} , comment_id {comment_id} , valid {valid} , username {username}'} 
   


    
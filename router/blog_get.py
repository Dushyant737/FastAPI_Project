from fastapi import APIRouter , status , Response
from typing import Optional
from enum import Enum

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

@router.get('/all')
def get_all_blogs(page =1, page_size:Optional[int]=None):
    return {'message':f'all {page_size} blog belongs to page {page} !'} 


@router.get('/{id}/comment_id/{comment_id}')
def get_comment(id : int, comment_id : int, valid:bool = True, username:Optional[str]=None):
    return {'message':f' blog_id {id} , comment_id {comment_id} , valid {valid} , username {username}'}    


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get_blogs_data(id:int , response:Response):
    if id > 5 :
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error' : f'blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message':f'blog with id {id} !'} 



@router.get('/all',tags=['Comments'])
def get_all_blogs_2():
    """
    Simulate retriving the blog
    - **id** mandatory path peremeter
    - **comment_id** mandatory path peremeter
    """  
    return {'message':'all blogs provided !'} 
from fastapi import APIRouter , status , Response, Depends
from typing import Optional
from enum import Enum
from router_db.db_blog_post import required_functionality

router_db = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

@router_db.get('/all')
def get_all_blogs(page =1, page_size:Optional[int]=None , req_parameter : dict = Depends(required_functionality)):
    return {'message':f'all {page_size} blog belongs to page {page} !' , "req":req_parameter} 


@router_db.get('/{id}/comment_id/{comment_id}')
def get_comment(id : int, comment_id : int, valid:bool = True, username:Optional[str]=None, req_parameter : dict = Depends(required_functionality)):
    return {'message':f' blog_id {id} , comment_id {comment_id} , valid {valid} , username {username}'}    


@router_db.get('/{id}', status_code=status.HTTP_200_OK)
def get_blogs_data(id:int , response:Response , req_parameter : dict = Depends(required_functionality)):
    if id > 5 :
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error' : f'blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message':f'blog with id {id} !'} 



@router_db.get('/all',tags=['Comments'])
def get_all_blogs_2():
    """
    Simulate retriving the blog
    - **id** mandatory path peremeter
    - **comment_id** mandatory path peremeter
    """  
    return {'message':'all blogs provided !'} 
from fastapi import APIRouter , Query , Body , Path
from pydantic import BaseModel
from typing import Optional , List , Dict

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

# nothing will come in the request body
"""
@router.post('/new')
def create_blog():
    pass

"""

"""
class BlogModel(BaseModel):
    pass

@router.post('/new')
def create_blog(blog: BaseModel):
    return "Ok"
"""

"""
class BlogModel(BaseModel):
    title : str
    content : str
    nb_comments : int
    published : Optional[bool]
    name : str

@router.post('/new')
def create_blog(blog: BlogModel):
    # return "Ok"
    # return blog
    return {"Data":blog}

"""

# Path and query parameters in Post 

"""
class BlogModel(BaseModel):
    title : str
    name : str
    content : str
    nb_comments : int
    published : Optional[bool]
    

@router.post('/new/{id}')
def create_blog(blog: BlogModel , id : int , version : int =1 ):
    return {
        'id' : id,
        'Data':blog,
        'version' : version
        }
"""

# Program for metadata (Title, Descption, Alias)
    

"""
class BlogModel(BaseModel):
    title : str
    name : str
    content : str
    nb_comments : int
    published : Optional[bool]


@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel , id : int,
        comment_id: int = Query(None,
            title="Id of the comment",
            description="some description of the comment",
            alias="commentId",
            deprecated=True
        )):
    return {
        'blog' : blog,
        'id' : id,
        'Data':blog,
        'comment_id' : comment_id
        }
"""

# added body peremeter (optional, fixed, validator - max/min/regex)

"""

class BlogModel(BaseModel):
    title : str
    name : str
    content : str
    nb_comments : int
    published : Optional[bool]


@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel , id : int,
        comment_id: int = Query(None,
            title="Id of the comment",
            description="some description of the comment",
            alias="commentId",
            deprecated=True
        ),
        # content: str = Body("Hi, How are you ?") # it's optinal 
        # content: str = Body(Ellipsis)
        content: str = Body(...,
        min_length=2,
        max_length=6,
        regex='[a-z\s]*$',
        )
        
    ):   
    return {
        'blog' : blog,
        'id' : id,
        'Data':blog,
        'comment_id' : comment_id
        }
       
"""

# multiple values with list in query peremeters 

"""

class BlogModel(BaseModel):
    title : str
    name : str
    content : str
    nb_comments : int
    published : Optional[bool]


@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel , id : int,
        comment_id: int = Query(None,
            title="Id of the comment",
            description="some description of the comment",
            alias="commentId",
            deprecated=True
        ),
        # content: str = Body("Hi, How are you ?") # it's optinal 
        # content: str = Body(Ellipsis)
        content: str = Body(...,
        min_length=10,
        max_length=20,
        regex='[a-z\s]*$'
        ),
        # v: Optional[List[str]] = Query(None)
        v: Optional[List[str]] = Query(['1.0','1.1','1.2']),
        
    ): 

    return {
        'blog' : blog,
        'id' : id,
        'Data':blog,
        'comment_id' : comment_id,
        'Vesrion' : v,
        }
      
"""

# Number Peremeters

"""
class BlogModel(BaseModel):
    title : str
    name : str
    content : str
    nb_comments : int
    published : Optional[bool]


@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel , id : int,
        comment_title: int = Query(None,
            title="title of the comment",
            description="some description of the comment_title",
            alias="commentTitle",
            deprecated=True
        ),
        # content: str = Body("Hi, How are you ?") # it's optinal 
        # content: str = Body(Ellipsis)
        content: str = Body(...,
        min_length=10,
        max_length=20,
        regex='[a-z\s]*$'
        ),
        # v: Optional[List[str]] = Query(None)
        v: Optional[List[str]] = Query(['1.0','1.1','1.2']),
        comment_id: int = Path(None,gt=5, le=10)
    ): 

    return {
        'blog' : blog,
        'id' : id,
        'Data':blog,
        'comment_title' : comment_title,
        'Vesrion' : v,
        'comment_id' : comment_id
        }

"""

# complex subtypes



class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title : str
    name : str
    content : str
    nb_comments : int
    published : Optional[bool]
    tags : List[str] = []
    metadata : Dict[str,str] = {'key1' : 'value1'}
    image:Optional[Image] = None

@router.post('/new/{id}')
def create_blog(blog: BlogModel , id : int , version : int =1 ):
    return {
        'id' : id,
        'Data':blog,
        'version' : version
        }


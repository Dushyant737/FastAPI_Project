from fastapi import FastAPI
from router_db import db_blog_get
from router_db import db_blog_post
from router_db import models
from router_db.database import engine
from typing import Optional
from router_db import user

app = FastAPI()
app.include_router(db_blog_get.router_db)
app.include_router(db_blog_post.router_db)
app.include_router(user.router_db)


@app.get('/')
def hello_method():
    return {"Message" : "Welcome to FastAPI, This is database main 'router_db_main.py' !"}

models.Base.metadata.create_all(engine)

  
 
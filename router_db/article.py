from typing import List
from schemas import ArticleBase, ArticleDisplay, UserBase
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from router_db.database import get_db
from router_db import db_article

router_db = APIRouter(
  prefix='/article',
  tags=['article']
)

# Create article
@router_db.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
  return db_article.create_article(db, request)

# Get specific article
@router_db.get('/{id}') #, response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db)):
  return {
    'data': db_article.get_article(db, id)
  }
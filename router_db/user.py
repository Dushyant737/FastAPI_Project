from schemas import UserBase, UserDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from router_db.database import get_db
from router_db import db_user


router_db = APIRouter(
  prefix='/user',
  tags=['user']
)

# Create user
@router_db.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
  return db_user.create_user(db, request)

# Read user

# Update user

# Delete user
from router_db.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer , String , Boolean
from sqlalchemy.orm import relationship
# from sqlalchemy.sql.schema import ForeignKey

class DbUser(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String)
  email = Column(String)
  password = Column(String)

"""  
class DbArticle(Base):
  __tablename__= 'articles'
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  content = Column(String)
  published = Column(Boolean)
  user_id = Column(Integer, ForeignKey('users.id'))
  user = relationship("DbUser", back_populates='items')  
"""  
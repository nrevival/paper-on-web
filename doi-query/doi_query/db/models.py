from sqlalchemy import Column, String, Integer

from .config import Base

DOI_LIMIT_LENGTH = 255
CATEGORY_NAME_LENGTH = 50


class Paper(Base):
    __tablename__ = "paper"
    doi = Column(String(length=DOI_LIMIT_LENGTH))    
    url = Column(String)
    


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String(length=CATEGORY_NAME_LENGTH))

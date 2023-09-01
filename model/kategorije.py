from . import Base
from sqlalchemy import *

class Kategorija(Base):
    __tablename__ = "kategorije"
    id = Column(Integer, primary_key = True)
    ime = Column(String(50))
    
    
    
    
    
    
    

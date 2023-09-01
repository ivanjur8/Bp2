from . import Base
from sqlalchemy import *

class Recenzija(Base):
    __tablename__ = "recenzije"
    id = Column(Integer, primary_key=True)
    ocjena = Column(DECIMAL)
    komentar = Column(Text)
    #korisnik_id = Column(Integer, ForeignKey("korisnici.id"))
    proizvod_id = Column(Integer, ForeignKey("proizvodi.id"))


    
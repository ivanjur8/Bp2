from . import Base
from sqlalchemy import *


class Narudzba(Base):
    __tablename__ = "narudzbe"
    id = Column(Integer, primary_key = True)
    name =Column(String)
    #ukupna_cijena = Column(DECIMAL)
    datum_narudzbe = Column(DateTime ,nullable=True)
    status = Column(String(50),nullable=True)
    korisnik_id = Column(Integer, ForeignKey("korisnici.id"))
    proizvod_id = Column(Integer, ForeignKey("proizvodi.id"))



    


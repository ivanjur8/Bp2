from . import Base
from sqlalchemy import *

class Proizvod(Base):
    __tablename__ = "proizvodi"
    id = Column(Integer, primary_key=True)
    naziv = Column(String(50))
    cijena = Column(String(20))
    opis = Column(Text)
    kolicina = Column(String(50))
    stanje_na_skladistu = Column(Integer)
    datum_objave = Column(DateTime)
    ocjena = Column(DECIMAL)
    slika = Column(String(50))
    kategorija_id = Column(Integer, ForeignKey("kategorije.id"))


    



    
    
from . import Base
from sqlalchemy import *

class Promocija(Base):
    __tablename__ = "promocije"
    id = Column(Integer, primary_key = True)
    naziv = Column(String(50))
    opis = Column(Text)
    popust = Column(DECIMAL)
    datum_pocetka = Column(DateTime)
    datum_zavrsetka = Column(DateTime)
    proizvod_id = Column(Integer, ForeignKey("proizvodi.id"))

    
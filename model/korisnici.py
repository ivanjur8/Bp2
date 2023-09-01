from . import Base
from sqlalchemy import *

class Korisnik(Base):
    __tablename__ = "korisnici"
    id = Column(Integer, primary_key = True)
    ime = Column(String(50))
    prezime = Column(String(50))
    email = Column(String(100))
    korisnicko_ime = Column(String(50))
    lozinka = Column(String(50))




from sqlalchemy.orm import relationship

from .proizvodi import Proizvod
from .korisnici import Korisnik
from .kategorije import Kategorija
from .recenzije import Recenzija
from .promocije import Promocija
from .narudzbe import Narudzba
from . import Base
from . import engine

Kategorija.proizvodi = relationship("Proizvod", back_populates="kategorija")
#Recenzija.korisnik = relationship("Korisnik",back_populates="recencije")
Recenzija.proizvod = relationship("Proizvod",back_populates="recenzije")
Proizvod.kategorija = relationship("Kategorija", back_populates="proizvodi")
Narudzba.korisnik = relationship("Korisnik",back_populates="narudzbe")
Narudzba.proizvodi = relationship("Proizvod",back_populates="narudzbe")
#Korisnik.recenzije = relationship("Recenzija",back_populates="korisnik")
Korisnik.narudzbe = relationship("Narudzba", back_populates="korisnik")
Proizvod.recenzije = relationship("Recenzija",back_populates="proizvod")
Proizvod.promocije = relationship("Promocija",back_populates="proizvod")
Proizvod.narudzbe = relationship("Narudzba", back_populates="proizvodi")
Promocija.proizvod = relationship("Proizvod", back_populates="promocije")

Base.metadata.bind = engine
Base.metadata.create_all(bind=engine)
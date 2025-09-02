from pydantic import BaseModel

class FilmBase(BaseModel):
    titulo:str
    genero:str
    ano:int
    nota:float

class FilmeCreate(FilmBase):
    pass

class Filme(FilmBase):
    id_filme:int

class Config:
    orm_mode = True

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import schemas, crud
from db.database import get_db

router = APIRouter(prefix="/categorias", tags=["Categorias"])

@router.get("/")
def get_categorias(db: Session = Depends(get_db)):
    return crud.get_all_categorias(db)

@router.post("/", response_model=schemas.CategoriaEquipo)
def create_categoria(categoria: schemas.CategoriaEquipoCreate, db: Session = Depends(get_db)):
    return crud.create_categoria(db, categoria)

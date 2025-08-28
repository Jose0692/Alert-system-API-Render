from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import models, schemas
from db.database import get_db
from db import crud

router = APIRouter(prefix="/cines", tags=["Cines"])

@router.get("/")
def get_cines(db: Session = Depends(get_db)):
    return crud.get_all_cines(db)

@router.get("/zona/{id_zona}")
def get_cines_por_zona(id_zona: int, db: Session = Depends(get_db)):
    return crud.get_cines_by_zona(db, id_zona)

@router.post("/", response_model=schemas.Cine)
def create_cine(cine: schemas.CineCreate, db: Session = Depends(get_db)):
    nuevo_cine = models.Cine(**cine.dict())
    db.add(nuevo_cine)
    db.commit()
    db.refresh(nuevo_cine)
    return nuevo_cine
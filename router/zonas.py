from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import models, schemas
from db.database import get_db
from db import crud

router = APIRouter(prefix="/zonas", tags=["zonas"])

@router.get("/")
def get_zonas(db: Session = Depends(get_db)):
    return crud.get_all_zonas(db)

@router.get("/pais/{pais_id}")
def get_zonas_por_pais(pais_id: int, db: Session = Depends(get_db)):
    return crud.get_zonas_by_pais(db, pais_id)

@router.post("/", response_model=schemas.Zona)
def create_zona(zona: schemas.ZonaCreate, db: Session = Depends(get_db)):
    nueva_zona = models.Zona(**zona.dict())
    db.add(nueva_zona)
    db.commit()
    db.refresh(nueva_zona)
    return nueva_zona
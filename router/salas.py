from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import models, schemas
from db.database import get_db
from db import crud

router = APIRouter(prefix="/salas", tags=["Salas"])

@router.get("/")
def get_salas(db: Session = Depends(get_db)):
    return crud.get_all_salas(db)

@router.get("/cine/{cine_id}")
def get_salas_por_cine(cine_id: int, db: Session = Depends(get_db)):
    return crud.get_salas_by_cine(db, cine_id)

@router.post("/", response_model=schemas.Sala)
def create_sala(sala: schemas.SalaCreate, db: Session = Depends(get_db)):
    nueva_sala = models.Sala(**sala.dict())
    db.add(nueva_sala)
    db.commit()
    db.refresh(nueva_sala)
    return nueva_sala
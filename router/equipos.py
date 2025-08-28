from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import schemas, crud
from db.database import get_db

router = APIRouter(prefix="/equipos", tags=["Equipos"])

@router.get("/")
def get_equipos(db: Session = Depends(get_db)):
    return crud.get_all_equipos(db)

@router.get("/sala/{sala_id}")
def get_equipos_por_sala(sala_id: int, db: Session = Depends(get_db)):
    return crud.get_equipos_by_sala(db, sala_id)

@router.post("/", response_model=schemas.Equipo)
def create_equipo(equipo: schemas.EquipoCreate, db: Session = Depends(get_db)):
    return crud.create_equipo(db, equipo)
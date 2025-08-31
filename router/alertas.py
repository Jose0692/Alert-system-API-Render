from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import schemas, crud
from db.database import get_db

router = APIRouter(prefix="/alertas", tags=["Alertas"])

@router.get("/")
def get_alertas(db: Session = Depends(get_db)):
    return crud.get_all_alertas(db)

@router.get("/equipo/{equipo_id}")
def get_alertas_por_equipo(equipo_id: int, db: Session = Depends(get_db)):
    return crud.get_alertas_by_equipo(db, equipo_id)

@router.post("/", response_model=schemas.Alerta)
def create_alerta(alerta: schemas.AlertaCreate, db: Session = Depends(get_db)):
    return crud.create_alerta(db, alerta)
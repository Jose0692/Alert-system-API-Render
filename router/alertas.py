from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import schemas, crud
from db.database import get_db

router = APIRouter(prefix="/alertas", tags=["Alertas"])

@router.get("/")
def get_alertas(db: Session = Depends(get_db)):
    return crud.get_all_alertas(db)

@router.get("/{alerta_id}")
def get_alerta(alerta_id: int, db: Session = Depends(get_db)):
    alerta = crud.get_alerta_by_id(db, alerta_id)
    if alerta is None:
        raise HTTPException(status_code=404, detail="Alerta no encontrada")
    return alerta

@router.get("/equipo/{equipo_id}")
def get_alertas_por_equipo(equipo_id: int, db: Session = Depends(get_db)):
    return crud.get_alertas_by_equipo(db, equipo_id)

@router.get("/buscar/")
def buscar_alertas_por_codigo_equipo(codigo_alerta: str, equipo_id: int, db: Session = Depends(get_db)):
    return crud.get_alertas_by_codigo_equipo(db, codigo_alerta, equipo_id)

@router.post("/", response_model=schemas.Alerta)
def create_alerta(alerta: schemas.AlertaCreate, db: Session = Depends(get_db)):
    return crud.create_alerta(db, alerta)

@router.put("/{alerta_id}", response_model=schemas.Alerta)
def update_alerta(alerta_id: int, alerta_update: schemas.AlertaUpdate, db: Session = Depends(get_db)):
    db_alerta = crud.update_alerta(db, alerta_id, alerta_update)
    if db_alerta is None:
        raise HTTPException(status_code=404, detail="Alerta no encontrada")
    return db_alerta
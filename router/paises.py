from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import models, schemas
from db.database import get_db
from db import crud

router = APIRouter(prefix="/paises", tags=["Paises"])

@router.get("/")
def get_paises(db: Session = Depends(get_db)):
    return crud.get_all_paises(db)
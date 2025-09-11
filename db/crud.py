from sqlalchemy.orm import Session
from . import models, schemas

# Paises
def get_all_paises(db: Session):
    return db.query(models.Pais).all()

def get_pais_by_id(db: Session, id_pais: int):
    return db.query(models.Pais).filter(models.Pais.id == id_pais).first()

def create_pais(db: Session, pais: schemas.PaisCreate):
    nuevo_pais = models.Pais(nombre=pais.nombre)
    db.add(nuevo_pais)
    db.commit()
    db.refresh(nuevo_pais)
    return nuevo_pais

# Zonas
def get_all_zonas(db: Session):
    return db.query(models.Zona).all()

def get_zonas_by_pais(db: Session, id_pais: int):
    return db.query(models.Zona).filter(models.Zona.id_pais == id_pais).all()

def create_zona(db: Session, zona: schemas.ZonaCreate):
    nueva_zona = models.Zona(nombre=zona.nombre, id_pais=zona.id_pais)
    db.add(nueva_zona)
    db.commit()
    db.refresh(nueva_zona)
    return nueva_zona

# Cines
def get_all_cines(db: Session):
    return db.query(models.Cine).all()

def get_cines_by_zona(db: Session, id_zona: int):
    return db.query(models.Cine).filter(models.Cine.id_zona == id_zona).all()

def create_cine(db: Session, cine: schemas.CineCreate):
    nuevo_cine = models.Cine(nombre=cine.nombre, id_zona=cine.id_zona)
    db.add(nuevo_cine)
    db.commit()
    db.refresh(nuevo_cine)
    return nuevo_cine

# Salas
def get_all_salas(db: Session):
    return db.query(models.Sala).all()

def get_salas_by_cine(db: Session, id_cine: int):
    return db.query(models.Sala).filter(models.Sala.id_cine == id_cine).all()

def create_sala(db: Session, sala: schemas.SalaCreate):
    nueva_sala = models.Sala(nombre=sala.nombre, id_cine=sala.id_cine)
    db.add(nueva_sala)
    db.commit()
    db.refresh(nueva_sala)
    return nueva_sala

# Categoria equipos
def get_all_categorias(db: Session):
    return db.query(models.CategoriaEquipo).all()

def create_categoria(db: Session, categoria: schemas.CategoriaEquipoCreate):
    nueva_categoria = models.CategoriaEquipo(nombre_categoria_equipo=categoria.nombre_categoria_equipo)
    db.add(nueva_categoria)
    db.commit()
    db.refresh(nueva_categoria)
    return nueva_categoria

# Equipos
def get_all_equipos(db: Session):
    return db.query(models.Equipo).all()

def get_equipos_by_sala(db: Session, sala_id: int):
    return db.query(models.Equipo).filter(models.Equipo.id_sala == sala_id).all()

def create_equipo(db: Session, equipo: schemas.EquipoCreate):
    nuevo_equipo = models.Equipo(**equipo.dict())
    db.add(nuevo_equipo)
    db.commit()
    db.refresh(nuevo_equipo)
    return nuevo_equipo

# Alertas
def get_all_alertas(db: Session):
    return db.query(models.Alerta).all()

def get_alertas_by_equipo(db: Session, equipo_id: int):
    return db.query(models.Alerta).filter(models.Alerta.id_equipo == equipo_id).all()

def get_alerta_by_id(db: Session, alerta_id: int):
    return db.query(models.Alerta).filter(models.Alerta.id_alerta == alerta_id).first()

def get_alertas_by_codigo_equipo(db: Session, codigo_alerta: str, equipo_id: int):
    return db.query(models.Alerta).filter(
        models.Alerta.codigo_alerta == codigo_alerta,
        models.Alerta.id_equipo == equipo_id
    ).all()

def create_alerta(db: Session, alerta: schemas.AlertaCreate):
    nueva_alerta = models.Alerta(**alerta.dict())
    db.add(nueva_alerta)
    db.commit()
    db.refresh(nueva_alerta)
    return nueva_alerta

def update_alerta(db: Session, alerta_id: int, alerta_update: schemas.AlertaUpdate):
    db_alerta = db.query(models.Alerta).filter(models.Alerta.id_alerta == alerta_id).first()
    if db_alerta:
        update_data = alerta_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_alerta, field, value)
        db.commit()
        db.refresh(db_alerta)
    return db_alerta

def get_numero_alertas_error(db: Session):
    return db.query(models.Alerta).filter(models.Alerta.tipo_alerta == "Error").count()
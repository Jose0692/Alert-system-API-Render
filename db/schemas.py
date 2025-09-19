from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class PaisBase(BaseModel):
    num_cine: int 
    octeto_pais: int
    nombre: str

class PaisCreate(PaisBase):
    pass

class Pais(PaisBase):
    id_pais: int

    class Config:
        from_attributes = True

class ZonaBase(BaseModel):
    nombre_zona: str
    correo_zona: str
    id_pais: int

class ZonaCreate(ZonaBase):
    pass

class Zona(ZonaBase):
    id_zona: int

    class Config:
        from_attributes = True


class CineBase(BaseModel):
    nombre_cine: str
    ubicacion_cine: Optional[str] = None
    num_cine: Optional[str] = None
    estado_cine: Optional[str] = None
    id_zona: int

class CineCreate(CineBase):
    pass

class Cine(CineBase):
    id_cine: int

    class Config:
        from_attributes = True


class SalaBase(BaseModel):
    numero_sala: int
    capacidad_sala: Optional[int] = None
    estado_sala: Optional[str] = None
    id_cine: int

class SalaCreate(SalaBase):
    pass

class Sala(SalaBase):
    id_sala: int

    class Config:
        from_attributes = True

# ---------- CATEGORIA EQUIPO ----------
class CategoriaEquipoBase(BaseModel):
    nombre_categoria_equipo: str


class CategoriaEquipoCreate(CategoriaEquipoBase):
    pass


class CategoriaEquipo(CategoriaEquipoBase):
    id_categoria_equipo: int

    class Config:
        from_attributes = True


# ---------- EQUIPO ----------
class EquipoBase(BaseModel):
    nombre_equipo: str
    marca_equipo: Optional[str] = None
    modelo_equipo: Optional[str] = None
    ip_equipo: Optional[str] = None
    fecha_mantenimiento_equipo: Optional[date] = None
    fecha_instalacion_equipo: Optional[date] = None
    estado_equipo: Optional[str] = None
    hora_restante_equipo_1: int
    hora_uso_equipo_1: int
    modelo_consum_equipo_1: Optional[str] = None
    hora_restante_equipo_2: int
    hora_uso_equipo_2: int
    modelo_consum_equipo_2: Optional[str] = None
    hora_restante_equipo_3: int
    hora_uso_equipo_3: int
    modelo_consum_equipo_3: Optional[str] = None
    id_sala: int
    id_categoria_equipo: int


class EquipoCreate(EquipoBase):
    pass


class Equipo(EquipoBase):
    id_equipo: int

    class Config:
        from_attributes = True


# ---------- ALERTA ----------
class AlertaBase(BaseModel):
    # Campos OBLIGATORIOS
    id_equipo: int
    
    # Campos OPCIONALES (pueden ser null en la BD)
    tipo_alerta: Optional[str] = None
    mensaje_alerta: Optional[str] = None
    criticidad_alerta: Optional[str] = None
    estado_alerta: Optional[str] = None
    codigo_alerta: Optional[str] = None
    showstopper_alerta: Optional[str] = None
    silencio_alerta: Optional[str] = None
    maintenence_alert: Optional[str] = None

    # fecha_hora_alerta NO se incluye porque se auto-genera

class AlertaCreate(AlertaBase):
    pass

class AlertaUpdate(BaseModel):
    # Campos que se pueden actualizar
    tipo_alerta: Optional[str] = None
    mensaje_alerta: Optional[str] = None
    criticidad_alerta: Optional[str] = None
    estado_alerta: Optional[str] = None
    codigo_alerta: Optional[str] = None
    showstopper_alerta: Optional[str] = None
    silencio_alerta: Optional[str] = None
    maintenence_alert: Optional[str] = None

class AlertaResponse(AlertaBase):
    id_alerta: int
    fecha_hora_alerta: datetime
    
    class Config:
        from_attributes = True


class Alerta(AlertaBase):
    id_alerta: int

    class Config:
        from_attributes = True
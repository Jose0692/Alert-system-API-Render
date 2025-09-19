from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import INET
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Pais(Base):
    __tablename__ = "paises"
    id_pais = Column(Integer, primary_key=True, index=True)
    octeto_pais = Column(Integer)
    nombre_pais = Column(String(100), nullable=False)
    zonas = relationship("Zona", back_populates="pais", cascade="all, delete")

class Zona(Base):
    __tablename__ = "zonas"
    id_zona = Column(Integer, primary_key=True, index=True)
    nombre_zona = Column(String(100), nullable=False)
    correo_zona = Column(String(100), nullable=False)
    id_pais = Column(Integer, ForeignKey("paises.id_pais", ondelete="CASCADE"), nullable=False)
    pais = relationship("Pais", back_populates="zonas")
    cines = relationship("Cine", back_populates="zona", cascade="all, delete")

class Cine(Base):
    __tablename__ = "cines"
    id_cine = Column(Integer, primary_key=True, index=True)
    nombre_cine = Column(String(150), nullable=False)
    ubicacion_cine = Column(String(255))
    num_cine = Column(Integer)
    estado_cine = Column(String(255))
    id_zona = Column(Integer, ForeignKey("zonas.id_zona", ondelete="CASCADE"), nullable=False)
    zona = relationship("Zona", back_populates="cines")
    salas = relationship("Sala", back_populates="cine", cascade="all, delete")

class Sala(Base):
    __tablename__ = "salas"
    id_sala = Column(Integer, primary_key=True, index=True)
    numero_sala = Column(Integer, nullable=False)
    capacidad_sala = Column(Integer)
    estado_sala = Column(String(255))
    id_cine = Column(Integer, ForeignKey("cines.id_cine", ondelete="CASCADE"), nullable=False)
    cine = relationship("Cine", back_populates="salas")
    equipos = relationship("Equipo", back_populates="sala", cascade="all, delete")

class CategoriaEquipo(Base):
    __tablename__ = "categoria_equipo"
    id_categoria_equipo = Column(Integer, primary_key=True, index=True)
    nombre_categoria_equipo = Column(String(100), nullable=False)
    equipos = relationship("Equipo", back_populates="categoria", cascade="all, delete")

class Equipo(Base):
    __tablename__ = "equipos"
    id_equipo = Column(Integer, primary_key=True, index=True)
    nombre_equipo = Column(String(150), nullable=False)
    marca_equipo = Column(String(100))
    modelo_equipo = Column(String(100))
    ip_equipo = Column(INET)
    fecha_mantenimiento_equipo = Column(Date)
    fecha_instalacion_equipo = Column(Date)
    estado_equipo = Column(String(255))
    hora_restante_equipo_1 = Column(Integer)
    hora_uso_equipo_1 = Column(Integer)
    modelo_consum_equipo_1 = Column(String(255))
    hora_restante_equipo_2 = Column(Integer)
    hora_uso_equipo_2 = Column(Integer)
    modelo_consum_equipo_2 = Column(String(255))
    hora_restante_equipo_3 = Column(Integer)
    hora_uso_equipo_3 = Column(Integer)
    modelo_consum_equipo_3 = Column(String(255))
    id_sala = Column(Integer, ForeignKey("salas.id_sala", ondelete="CASCADE"), nullable=False)
    id_categoria_equipo = Column(Integer, ForeignKey("categoria_equipo.id_categoria_equipo", ondelete="CASCADE"), nullable=False)
    sala = relationship("Sala", back_populates="equipos")
    categoria = relationship("CategoriaEquipo", back_populates="equipos")
    alertas = relationship("Alerta", back_populates="equipo", cascade="all, delete")

class Alerta(Base):
    __tablename__ = "alertas"
    id_alerta = Column(Integer, primary_key=True, index=True)
    tipo_alerta = Column(String(100))
    mensaje_alerta = Column(Text)
    criticidad_alerta = Column(String(50))
    fecha_hora_alerta = Column(TIMESTAMP, server_default=func.now())
    estado_alerta = Column(String(50))
    codigo_alerta = Column(String(50))
    showstopper_alerta = Column(String(100))
    silencio_alerta = Column(String(100))
    maintenence_alert = Column(String(100))
    id_equipo = Column(Integer, ForeignKey("equipos.id_equipo", ondelete="CASCADE"), nullable=False)
    equipo = relationship("Equipo", back_populates="alertas")
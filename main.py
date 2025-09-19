from fastapi import FastAPI, Depends
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import select
from db.database import get_db, Base, engine
import db.models as models
import os
from db.database import engine
from db import models
from router import paises, zonas, cines, salas, categoria_equipos, equipos, alertas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir routers
app.include_router(paises.router)
app.include_router(zonas.router)
app.include_router(cines.router)
app.include_router(salas.router)
app.include_router(categoria_equipos.router)
app.include_router(equipos.router)
app.include_router(alertas.router)

# Montar carpeta de archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return FileResponse("templates/dashboard.html")

@app.get("/consumibles", response_class=HTMLResponse)
async def read_root():
    return FileResponse("templates/consumibles.html")

@app.get("/mapas", response_class=HTMLResponse)
async def get_dashboard():
    return FileResponse("templates/mapas.html")

@app.get("/favicon.ico")
def favicon():
    return FileResponse(os.path.join("static", "favicon.ico"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
from fastapi import FastAPI
from routers import ocr, bg
from routers import detect
from routers import auth
from database import Base, engine
from models import users

app = FastAPI()
app.include_router(ocr.router)
app.include_router(bg.router)
app.include_router(detect.router)
app.include_router(auth.router)

Base.metadata.create_all(bind=engine)
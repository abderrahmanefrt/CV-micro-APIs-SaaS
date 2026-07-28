from fastapi import FastAPI
from routers import ocr, bg
from routers import detect
from database import Base, engine
from models import users

app = FastAPI()
app.include_router(ocr.router)
app.include_router(bg.router)
app.include_router(detect.router)

Base.metadata.create_all(bind=engine)
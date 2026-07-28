from fastapi import FastAPI
from routers import ocr, bg

app = FastAPI()
app.include_router(ocr.router)
app.include_router(bg.router)
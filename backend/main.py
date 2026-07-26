from fastapi import FastAPI
from routers import ocr

app = FastAPI()
app.include_router(ocr.router)

@app.get("/")
def root():
    return {"message": "API is running"}
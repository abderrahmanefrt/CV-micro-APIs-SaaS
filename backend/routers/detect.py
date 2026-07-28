from fastapi import APIRouter, File, UploadFile
from services.detect_service import detecter_objets

router = APIRouter()

@router.post("/api/detect-objects")
async def detect_objects(file: UploadFile = File(...)):
    image_bytes = await file.read()
    resultats = detecter_objets(image_bytes)
    return {"detections": resultats}
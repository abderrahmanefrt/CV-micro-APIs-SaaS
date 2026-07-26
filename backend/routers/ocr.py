from fastapi import APIRouter, UploadFile, File
from services.ocr_service import extraire_texte

router = APIRouter()

@router.post("/api/ocr")
async def ocr_endpoint(file: UploadFile = File(...)):
    image_bytes = await file.read()
    texte = extraire_texte(image_bytes)
    return {"texte_extrait": texte}
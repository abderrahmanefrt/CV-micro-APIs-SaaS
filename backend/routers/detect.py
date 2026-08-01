from fastapi import APIRouter, File, UploadFile, Depends
from sqlalchemy.orm import Session
from services.auth_service import verifier_api_key, get_db
from models.users import User
from services.detect_service import detecter_objets

router = APIRouter()

@router.post("/api/detect-objects")
async def detect_objects(file: UploadFile = File(...), utilisateur: User = Depends(verifier_api_key), db: Session = Depends(get_db)):
    image_bytes = await file.read()
    resultats = detecter_objets(image_bytes)
    return {"detections": resultats}
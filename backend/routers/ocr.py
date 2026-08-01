from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from services.ocr_service import extraire_texte
from services.auth_service import verifier_api_key, get_db
from models.users import User

router = APIRouter()

@router.post("/api/ocr")
async def ocr_endpoint(
    file: UploadFile = File(...),
    utilisateur: User = Depends(verifier_api_key),
    db: Session = Depends(get_db)
):
    image_bytes = await file.read()
    texte = extraire_texte(image_bytes)
    
    utilisateur.credits -= 1
    db.commit()
    
    return {"texte_extrait": texte, "credits_restants": utilisateur.credits}
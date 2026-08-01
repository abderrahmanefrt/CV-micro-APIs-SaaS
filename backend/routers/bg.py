from fastapi import APIRouter, UploadFile, File, Depends
from fastapi.responses import Response
from services.bg_service import enlever_fond
from services.ocr_service import extraire_texte
from services.auth_service import verifier_api_key, get_db
from sqlalchemy.orm import Session
from models.users import User

router = APIRouter()

@router.post("/api/remove-bg")
async def remove_bg_endpoint(file: UploadFile = File(...) ,utilisateur: User = Depends(verifier_api_key),
    db: Session = Depends(get_db)):
    image_bytes = await file.read()
    image_sans_fond = enlever_fond(image_bytes)
    return Response(content=image_sans_fond, media_type="image/png")
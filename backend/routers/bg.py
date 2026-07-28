from fastapi import APIRouter, UploadFile, File
from fastapi.responses import Response
from services.bg_service import enlever_fond

router = APIRouter()

@router.post("/api/remove-bg")
async def remove_bg_endpoint(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image_sans_fond = enlever_fond(image_bytes)
    return Response(content=image_sans_fond, media_type="image/png")
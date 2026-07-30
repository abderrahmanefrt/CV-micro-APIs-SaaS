from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal
from services.auth_service import create_user

router = APIRouter()

class UserCreate(BaseModel):
   email: str
   password: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/api/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    nouvel_utilisateur = creer_utilisateur(db, user.email, user.password)
    return {"email": nouvel_utilisateur.email, "api_key": nouvel_utilisateur.api_key}


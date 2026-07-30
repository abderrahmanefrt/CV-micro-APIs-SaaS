from sqlalchemy.orm import Session
from fastapi import Header, HTTPException, Depends
from passlib.context import CryptContext
from models.users import User
from utils.apigen import generer_api_key
from database import SessionLocal


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(db: Session, email: str ,password: str) -> User:
    hashed_password =pwd_context.hash(password)
    api_key = generer_api_key()
    new_user = User(email=email, hashed_password=hashed_password, api_key=api_key ,credits=100)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_db():
  db = SessionLocal()
  try:
      yield db
  finally:
      db.close()

def verifier_api_key(x_api_key: str = Header(...), db: Session = Depends(get_db)) -> User:
    utilisateur = db.query(User).filter(User.api_key == x_api_key).first()
    
    if not utilisateur:
        raise HTTPException(status_code=401, detail="Clé API invalide")
    
    if utilisateur.credits <= 0:
        raise HTTPException(status_code=402, detail="Crédits épuisés")
    
    return utilisateur
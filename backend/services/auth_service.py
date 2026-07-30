from sqlalchemy.orm import Session
from passlib.context import CryptContext
from models.users import User
from utils.apigen import generer_api_key

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(db: Session, email: str ,password: str) -> User:
    hashed_password =pwd_context.hash(password)
    api_key = generer_api_key()
    new_user = User(email=email, hashed_password=hashed_password, api_key=api_key ,credits=100)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
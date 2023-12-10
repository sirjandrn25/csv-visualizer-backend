from sqlalchemy.orm import Session

from csv_visualizer_api.utils import make_hash
from csv_visualizer_api.models import User,CsvFile
from csv_visualizer_api.schemas import UserCreate


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed_password =  make_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



def get_user_files(db: Session, user_id: int ,skip: int = 0, limit: int = 100):
    return db.query(CsvFile).filter(User.user_id==user_id).offset(skip).limit(limit).all()
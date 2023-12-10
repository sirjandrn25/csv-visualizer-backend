
import pandas as pd
import json
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session


from csv_visualizer_api.schemas import CsvFileCreate,UserCreate,CsvFile,User
from csv_visualizer_api.crud import get_user_by_email, get_user, create_user
from csv_visualizer_api.database import SessionLocal, engine
from .models import Base

Base.metadata.create_all(bind=engine)
from fastapi import Depends, FastAPI, HTTPException

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()
origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return {"Hello": "World"}

file_url = './employee_demo.csv'
@app.get('/file-table-info')
def visualize_csv_file():
    try:
        df = pd.read_csv(file_url)
        table_form = json.loads(df.to_json(orient='table', index=False))
        return table_form
    except Exception as e:
        print(e)
        return e
 
@app.get('/file-meta-info')
def visualize_csv_file():
    try:
        df = pd.read_csv(file_url)
        meta_info = df.describe().to_json()
        return json.loads(meta_info)
    except Exception as e:
        print(e)
        return e

class CsvUploaderModel(BaseModel):
    __tablename__ = "users"
    name: str
    file_url:str
    user_id:str | None
@app.post('/csv-uploader')
def csv_uploader(data: CsvUploaderModel):

    return  
    

@app.post("/users", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)
@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
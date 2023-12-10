
import pandas as pd
import json
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI



# Dependency



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

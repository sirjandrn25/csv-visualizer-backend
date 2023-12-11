
import pandas as pd
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Union


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

demo_file_url =  "https://csv-visualizer.s3.us-east-1.amazonaws.com/employee_demo.csv-8239"
@app.get('/file-table-info')
def visualize_csv_file(q: Union[str, None] = demo_file_url):


    try:
        df = pd.read_csv(q)
        table_form = json.loads(df.to_json(orient='table', index=False))
        return table_form
    except Exception as e:
        print(e)
        return e
 
@app.get('/file-meta-info')
def visualize_csv_file(q: Union[str, None] = demo_file_url):
    try:
        df = pd.read_csv(q)
        meta_info = df.describe().to_json()
        return json.loads(meta_info)
    except Exception as e:
        print(e)
        return e

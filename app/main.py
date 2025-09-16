from fastapi import FastAPI, HTTPException, status, Depends
from typing import List
from random import randrange
import os
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas, utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .routers import post, user, auth



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
    
while True:
    try:
        conn = psycopg2.connect(host='localhost', database='postgres', user='postgres', password=os.getenv('tpass'), cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful!")
        break
    
    except Exception as error:
        print("Connecting to database failed")
        print("Error:", error)
        time.sleep(2)
        
        
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
        
@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI application!"}        





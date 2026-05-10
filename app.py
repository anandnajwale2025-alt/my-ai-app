from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Cloud Run OK"}

@app.get("/health")
def health():
    return {"health": "ok"}
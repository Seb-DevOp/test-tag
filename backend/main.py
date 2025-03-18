from scripts.ModelManagement import ModelManagement
from fastapi import FastAPI
import os

app = FastAPI()

# Bonnes pratiques : Utiliser un chemin relatif au fichier main.py
model_path = "kdd_model.pkl"

dm = ModelManagement(0, 0)
dm.load(model_path)

@app.get("/test_model")
def test_model_loading():
    if dm.model:
        return {"message": "Le modèle a été chargé avec succès"}
    else:
        return {"message": "Erreur lors du chargement du modèle"}

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}
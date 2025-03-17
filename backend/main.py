from backend.scripts import ModelManagement
from fastapi import FastAPI

app = FastAPI()

dm = ModelManagement(0,0)
dm.load("kdd_model.pkl")

@app.get("/test_model")
def test_model_loading():
    if dm.model:
        return {"message": "Le modèle a été chargé avec succès"}
    else:
        return {"message": "Erreur lors du chargement du modèle"}

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

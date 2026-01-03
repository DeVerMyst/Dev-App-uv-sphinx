"""
Introduction au packaging
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field
from models.models import FakeIAModel
from modules.modules import read_config_file

app = FastAPI(title="API d'Apprentissage UV")

# --- Schéma Pydantic (Data Model) ---
class InferenceRequest(BaseModel):
    """
    Schéma de données pour la requête d'inférence.
    """
    prompt: str = Field(..., example="Bonjour l'IA !", description="Texte envoyé au modèle")

# --- Initialisation du faux modèle ---
ia_model = FakeIAModel()

@app.get("/")
async def root():
    """
    Route principale de l'API.

    Retourne un message de bienvenue simple.
    """
    return {"message": "Bienvenue sur l'API de formation UV/Sphinx !"}

@app.post("/predict")
async def get_prediction(request: InferenceRequest):
    """
    Route d'inférence IA.

    Prend un prompt, utilise le FakeIAModel et retourne la prédiction.
    """
    prediction = ia_model.predict(request.prompt)
    return {"status": "success", "data": prediction}

@app.get("/version")
async def get_version():
    """
    Récupère la version du projet depuis un fichier texte via le module utilitaire.
    """
    # On imagine un fichier version.txt à la racine
    try:
        content = read_config_file("version.txt")
        return {"version": content}
    except FileNotFoundError:
        return {"version": "1.0.0 (fichier non trouvé)"}
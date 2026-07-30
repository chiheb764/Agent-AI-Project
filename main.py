from fastapi import FastAPI
from agent import agent 
from pydantic import BaseModel
class QuestionRequest(BaseModel):
 question: str
app = FastAPI()
@app.get("/")
def accueil():
    return {
    "message":
    "Bienvenue dans l'Agent IA"
    }
@app.get("/bonjour")
def bonjour():
    return {
    "message": "Bonjour"
    }
@app.get("/status")
def status():
    return {
    "status": "OK"
    }
@app.get("/info")
def info():
    return {
    "application": "Agent IA",
    "version": "1.0"
    }
@app.get("/utilisateur/{nom}")
@app.post("/question")
def poser_question(
request: QuestionRequest
):
 pass
def utilisateur(nom):

    return {
    "message": f"Bonjour {nom}"
    }
@app.post("/question")
def poser_question(
    request: QuestionRequest
    ):
    resultat = agent.invoke(
    {
    "question":
    request.question
    }
    )
    return resultat
from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
import requests
import os
from pydantic import BaseModel

app = FastAPI()

class ChaveApiRequest(BaseModel):
    chave_api: str

# Montando o diretório de arquivos estáticos corretamente
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")), name="static")

templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

def validar_chave_api(chave_api):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address=New+York&key={chave_api}"
    resposta = requests.get(url)
    dados = resposta.json()

    if resposta.status_code == 200:
        if 'error_message' in dados:
            return False, dados['error_message']
        return True, "Chave API válida!"
    else:
        return False, f"Erro na requisição: {resposta.status_code}"

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/verificar")
async def verificar_chave(chave_api_request: ChaveApiRequest):
    chave_api = chave_api_request.chave_api
    valido, mensagem = validar_chave_api(chave_api)
    return {"valido": valido, "mensagem": mensagem}

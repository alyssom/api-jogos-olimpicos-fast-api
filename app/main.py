import email
from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def raiz():
    return {"message": "Retorno Raiz FastAPI."}

class Usuario(BaseModel):
    id: int
    email: str
    senha: str

data_base = [
    Usuario(id=1, email="alyssommartins@gmail.com", senha="12345"),
    Usuario(id=2, email="asommartins@icloud.com", senha="54321")
]

#Find All
@app.get("/usuarios")
def get_todos_os_usuarios():
    return data_base


#Find By Id
@app.get("/usuarios/{id_usuario}")
def get_usuario_por_id(id_usuario: int):
    for usuario in data_base:
        if(usuario.id == id_usuario):
            return usuario
    return {"Status:": 404, "Mensagem": "Usuário não encontrado."} 

#Insert New User
@app.post("/usuarios")
def insere_usuario(usuario: Usuario):
    data_base.append(usuario)
    return usuario

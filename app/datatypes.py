from datetime import date
from pydantic import BaseModel

class CompeticaoRequest(BaseModel):
    nome_competicao: str
    data_inicio: date
    data_encerramento: date

class ResultadoCompeticaoRequest(BaseModel):
    nome_atleta: str
    unidade: str
    valor: float
    nome_competicao: str
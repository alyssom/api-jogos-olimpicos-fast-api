from datetime import date
from pydantic import BaseModel

class CompeticaoRequest(BaseModel):
    nome_competicao: str
    data_inicio: date

class ResultadoCompeticaoRequest(BaseModel):
    nome_atleta: str
    unidade: str
    valor: float
    nome_competicao: str

class ResultadoCompeticao:
    nome_atleta: str
    valor: float

    def __init__(self, nome_atleta, valor):
        self.nome_atleta = nome_atleta
        self.valor = valor
    
class ResponseRanking:
    situacao: str
    resultados: list = ResultadoCompeticao
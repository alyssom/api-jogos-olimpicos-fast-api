from datetime import date
from pydantic import BaseModel

class CompeticaoRequest(BaseModel):
    nome_competicao: str
    data_inicio: date
    data_encerramento: date

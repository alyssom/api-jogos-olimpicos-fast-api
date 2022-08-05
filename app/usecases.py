
from xmlrpc.client import Boolean
from app.crud import busca_competicao
from app.database import SessionLocal

class ValidaCompeticao:
    existente: Boolean = True
    encerrada: Boolean = True

def competicao_is_ativa_existente(nome_competicao: str, db: SessionLocal):
    result = busca_competicao(nome_competicao,db)
    if result is not None:
        return True

def valida_competicao_existente(nome_competicao: str, db: SessionLocal):
    result = busca_competicao(nome_competicao,db)
    if result is None:
        ValidaCompeticao.existente = False
    if hasattr(result, 'data_encerramento'):
        ValidaCompeticao.encerrada = True
    return ValidaCompeticao

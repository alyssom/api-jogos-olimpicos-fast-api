
from unittest import result
from xmlrpc.client import Boolean
from app.crud import busca_resultado_final_competicao_tempo
from app.crud import busca_resultado_competicao_por_nome
from app.crud import busca_competicao
from app.database import SessionLocal

class ValidaCompeticao:
    existente: Boolean = True
    encerrada: Boolean = False

def competicao_is_ativa_existente(nome_competicao: str, db: SessionLocal):
    result = busca_competicao(nome_competicao,db)
    if result is not None:
        return True

def valida_competicao_existente(nome_competicao: str, db: SessionLocal):
    result = busca_competicao(nome_competicao,db)
    if result is None:
        ValidaCompeticao.existente = False
    if result.data_encerramento is not None:
        ValidaCompeticao.encerrada = True
    return ValidaCompeticao

def gera_resultado_competicao(nome_competicao: str, db: SessionLocal):
    result = busca_resultado_competicao_por_nome(nome_competicao, db)
    if result is not None:
        if result[0].unidade == 's':
            resultado_competicao = busca_resultado_final_competicao_tempo(nome_competicao,db)
    return resultado_competicao

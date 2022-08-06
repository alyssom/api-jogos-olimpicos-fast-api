
from app.dataprovider import busca_resultado_parcial_competicao_metros_por_nome
from app.dataprovider import busca_resultado_parcial_competicao_tempo_por_nome
from app.datatypes import ResponseRanking
from app.datatypes import ResultadoCompeticao
from app.dataprovider import busca_resultados_atleta_competicao
from app.datatypes import ResultadoCompeticaoRequest
from app.dataprovider import busca_resultado_final_competicao_metros, busca_resultado_final_competicao_tempo
from app.dataprovider import busca_resultado_competicao_por_nome
from app.dataprovider import busca_competicao
from app.database import SessionLocal


class ValidaCompeticao:
    existente: bool = True
    encerrada: bool = False

def competicao_is_ativa_existente(nome_competicao: str, db: SessionLocal):
    result = busca_competicao(nome_competicao,db)
    if result is not None:
        return True

def valida_competicao_existente(nome_competicao: str, db: SessionLocal):
    result = busca_competicao(nome_competicao,db)
    if result is None:
        ValidaCompeticao.existente = False
        return ValidaCompeticao
    if result.data_encerramento is not None:
        ValidaCompeticao.encerrada = True
    return ValidaCompeticao

def valida_atleta(resultado_competicao: ResultadoCompeticaoRequest, db: SessionLocal):
    if resultado_competicao.unidade == "m":
        tentativa_atleta = busca_resultados_atleta_competicao(resultado_competicao.nome_atleta, resultado_competicao.nome_competicao, db)
        if len(tentativa_atleta) == 3:
            return True
    if resultado_competicao.unidade == "s":
        tentativa_atleta = busca_resultados_atleta_competicao(resultado_competicao.nome_atleta, resultado_competicao.nome_competicao, db)
        if len(tentativa_atleta) != 0:
            return True
    return False

def valida_competicao_existe(nome_competicao: str, db: SessionLocal):
    result = busca_competicao(nome_competicao,db)
    if result is None:
        return True
    return False

def gera_resultado_competicao(nome_competicao: str, db: SessionLocal):
    response = ResponseRanking()
    competicao_db = busca_competicao(nome_competicao,db)
    resultado_competicao_db = busca_resultado_competicao_por_nome(nome_competicao, db)
    if competicao_db is not None and competicao_db.data_encerramento is not None:
        if resultado_competicao_db[0].unidade == 's':
            resultado_db = busca_resultado_final_competicao_tempo(nome_competicao,db)
            response.situacao = "Ranking Final"
            response.resultados = list(map(lambda resultado: ResultadoCompeticao(resultado[0], resultado[1]), resultado_db)) 
            return response
        if resultado_competicao_db[0].unidade == 'm':
            resultado_db = busca_resultado_final_competicao_metros(nome_competicao,db)
            response.situacao = "Ranking Final"
            response.resultados = list(map(lambda resultado: ResultadoCompeticao(resultado[0], resultado[1]), resultado_db)) 
            return response
    if resultado_competicao_db is not None and resultado_competicao_db[0].unidade == 's':
        resultado_db = busca_resultado_parcial_competicao_tempo_por_nome(nome_competicao, db)
        response.situacao = "Ranking Parcial"
        response.resultados = list(map(lambda resultado: ResultadoCompeticao(resultado[0], resultado[1]), resultado_db)) 
        return response
    if resultado_competicao_db is not None and resultado_competicao_db[0].unidade == 'm':
        resultado_db = busca_resultado_parcial_competicao_metros_por_nome(nome_competicao, db)
        response.situacao = "Ranking Parcial"
        response.resultados = list(map(lambda resultado: ResultadoCompeticao(resultado[0], resultado[1]), resultado_db)) 
        return response

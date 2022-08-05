from datetime import date
from typing import Generator
from sqlalchemy import null

from sqlalchemy.orm import Session
from app.datatypes import CompeticaoRequest, ResultadoCompeticaoRequest

from app.models import Competicao, ResultadoCompeticao

competicao = Competicao
resultadoCompeticao = ResultadoCompeticao


def cria_competicao(db: Session, competicaoRequest: CompeticaoRequest):
    nova_competicao = Competicao()
    nova_competicao.nome_competicao = competicaoRequest.nome_competicao
    nova_competicao.data_inicio = competicaoRequest.data_inicio
    db.add(nova_competicao)
    db.commit()

    db.refresh(nova_competicao)

    return nova_competicao


def cria_resultado_competicao(db: Session, resultadoCompeticaoRequest: ResultadoCompeticaoRequest):
    novo_resultado = ResultadoCompeticao()
    novo_resultado.nome_competicao_fk = resultadoCompeticaoRequest.nome_competicao
    novo_resultado.nome_atleta = resultadoCompeticaoRequest.nome_atleta
    novo_resultado.unidade = resultadoCompeticaoRequest.unidade
    novo_resultado.valor = resultadoCompeticaoRequest.valor

    db.add(novo_resultado)
    db.commit()

    db.refresh(novo_resultado)

    return novo_resultado

def encerra_competicao(
    nome_competicao: str, db: Session
):
    """
    Atualiza o registro de um estudante a partir do seu _id_ usando os
    novos valores em `values`.
    """
    # verifica se o estudante existe...
    if competicaodb := busca_competicao(nome_competicao, db):
        # altera os valores e submete as alterações
        data_encerramento = date.today()
        db.query(competicao).filter(competicao.nome_competicao == nome_competicao).update({"data_encerramento": data_encerramento}, synchronize_session="fetch")
        db.commit()

        # atualiza o conteúdo antes de enviá-lo de volta
        db.refresh(competicaodb)

        return competicaodb

def busca_todas_competicoes(db: Session) -> Generator:
    return db.query(competicao).all()

def busca_resultado_competicao(nome_competicao: str, db: Session) -> Generator:
    return db.query(resultadoCompeticao).filter(resultadoCompeticao.nome_competicao_fk == nome_competicao).first()

def busca_competicao(nome_competicao: str, db: Session) -> Generator:
    return db.query(competicao).filter(competicao.nome_competicao == nome_competicao).first()

def busca_resultado_final_competicao_tempo(nome_competicao: str, db: Session) -> Generator:
    resultado = db.query(resultadoCompeticao).order_by(resultadoCompeticao.valor).filter(resultadoCompeticao.nome_competicao_fk == nome_competicao).all()
    return resultado

def busca_resultado_competicao_por_nome(nome_competicao: str, db: Session) -> Generator:
    resultado = db.query(resultadoCompeticao).filter(resultadoCompeticao.nome_competicao_fk == nome_competicao).all()
    return resultado

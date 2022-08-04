from typing import Generator

from sqlalchemy.orm import Session
from app.datatypes import CompeticaoRequest, ResultadoCompeticaoRequest

from app.models import Competicao, ResultadoCompeticao

competicao = Competicao
resultadoCompeticao = ResultadoCompeticao


def cria_competicao(db: Session, competicaoRequest: CompeticaoRequest):
    nova_competicao = Competicao()
    nova_competicao.nome_competicao = competicaoRequest.nome_competicao
    nova_competicao.data_inicio = competicaoRequest.data_inicio
    nova_competicao.data_encerramento = competicaoRequest.data_encerramento
    db.add(nova_competicao)
    db.commit()

    db.refresh(nova_competicao)

    return nova_competicao


def cria_resltado_competicao(db: Session, resultadoCompeticaoRequest: ResultadoCompeticaoRequest):
    novo_resultado = ResultadoCompeticao()
    novo_resultado.nome_competicao_fk = resultadoCompeticaoRequest.nome_competicao
    novo_resultado.nome_atleta = resultadoCompeticaoRequest.nome_atleta
    novo_resultado.unidade = resultadoCompeticaoRequest.unidade
    novo_resultado.valor = resultadoCompeticaoRequest.valor

    db.add(novo_resultado)
    db.commit()

    db.refresh(novo_resultado)

    return novo_resultado


def busca_competicoes(db: Session) -> Generator:
    return db.query(competicao).all()

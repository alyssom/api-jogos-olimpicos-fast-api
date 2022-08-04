from typing import Generator

from sqlalchemy.orm import Session
from app.datatypes import CompeticaoRequest

from app.models import Competicao

competicao = Competicao


def cria_competicao(db: Session, competicaoRequest: CompeticaoRequest):
    nova_competicao = Competicao()
    nova_competicao.nome_competicao = competicaoRequest.nome_competicao
    nova_competicao.data_inicio = competicaoRequest.data_inicio
    nova_competicao.data_encerramento = competicaoRequest.data_encerramento
    db.add(nova_competicao)
    db.commit()

    db.refresh(nova_competicao)

    return nova_competicao


def busca_competicoes(db: Session) -> Generator:
    return db.query(competicao).all()

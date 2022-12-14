from datetime import datetime

import uvicorn
from app.usecases import valida_atleta, valida_competicao_existe
from app.usecases import gera_resultado_competicao
from app.dataprovider import busca_resultado_competicao
from app.dataprovider import encerra_competicao
from app.usecases import competicao_is_ativa_existente
from app.dataprovider import busca_todas_competicoes, cria_competicao, cria_resultado_competicao
from app.datatypes import CompeticaoRequest, ResultadoCompeticaoRequest

from app.database import Base, SessionLocal
from typing import Dict, Generator
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from app.database import engine
from app.usecases import valida_competicao_existente

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def raiz():
    return {"A API está no ar! Acesse /docs e tenha acesso ao Open API"}

@app.get("/competicoes/", status_code=status.HTTP_200_OK)
def buscar_todas_competicoes(db: Session = Depends(get_db)) -> Generator:
    if result := busca_todas_competicoes(db):
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Não existem competições cadastradas.",
    ) 

@app.get("/competicao/{nome_competicao}/ranking", status_code=status.HTTP_200_OK)
def buscar_ranking_competicao(nome_competicao: str, db: Session = Depends(get_db)) -> Generator:
    is_competicao_invalida = valida_competicao_existe(nome_competicao, db)
    if is_competicao_invalida == True:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "A Competição ao qual você deseja ver o Ranking ainda não foi cadastrada.") 
    
    if result := gera_resultado_competicao(nome_competicao, db):
        return result

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Não existem competições cadastradas.",
    ) 

@app.post(
    "/competicao/", status_code=status.HTTP_201_CREATED,
)
def cadatrar_competicao(
    competicao: CompeticaoRequest, db: Session = Depends(get_db),
):
    is_competicao_invalida = competicao_is_ativa_existente(competicao.nome_competicao, db)
    if is_competicao_invalida == True:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "A Competição ao qual você deseja cadastrar já esta cadastrada.") 
    if result := cria_competicao(db, competicao):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )  

@app.post(
    "/resultado-competicao/", status_code=status.HTTP_201_CREATED,
)
def cadatrar_resultado_competicao(
    resultado_competicao: ResultadoCompeticaoRequest, db: Session = Depends(get_db),
):  
    is_competicao_invalida = valida_competicao_existente(resultado_competicao.nome_competicao, db)
    if is_competicao_invalida.existente == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "A Competição ao qual você deseja cadastrar um resultado não existe.") 
    if is_competicao_invalida.encerrada == True:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "A Competição ao qual você deseja cadastrar o resultado já foi encerrada.") 
    is_atleta_invalido = valida_atleta(resultado_competicao, db)
    if is_atleta_invalido == True:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "Este atleta estourou o limite de tentativas nesta competição.") 
    
    if result := cria_resultado_competicao(db, resultado_competicao):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )  

@app.put(
    "/encerra/{nome_competicao}", status_code=status.HTTP_204_NO_CONTENT,
)
def encerrar_competicao(nome_competicao: str, db: Session = Depends(get_db)):
    if result := encerra_competicao(nome_competicao, db):
        gera_resultado_competicao(nome_competicao, db)
        return status.HTTP_204_NO_CONTENT

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Competição '{nome_competicao}' não encontrado.",
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")

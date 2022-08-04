from datetime import datetime

import uvicorn
from app.crud import busca_competicoes, cria_competicao, cria_resltado_competicao
from app.datatypes import CompeticaoRequest, ResultadoCompeticaoRequest

from app.database import Base, SessionLocal
from typing import Dict, Generator
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from app.database import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health/")
def vida() -> Dict[str, datetime]:
    return {"timestamp": datetime.now()}

@app.get("/competicoes/", status_code=status.HTTP_200_OK)
def busca_todas_competicoes(db: Session = Depends(get_db)) -> Generator:
    if result := busca_competicoes(db):
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
    print(resultado_competicao)
    if result := cria_resltado_competicao(db, resultado_competicao):
        return result

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )  


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

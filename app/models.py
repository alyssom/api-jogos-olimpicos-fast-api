from sqlalchemy import Column, Float, String, Date, Integer, ForeignKey

from app.database import Base


class Competicao(Base):
    __tablename__ = 'competicao'
    nome_competicao = Column(String(70), primary_key=True)
    data_inicio = Column(Date)
    data_encerramento = Column(Date)


class ResultadoCompeticao(Base):
    __tablename__ = 'resultados_competicoes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_atleta = Column(String(50))
    unidade = Column(String(5))
    valor = Column(Float)
    tentativa = Column(Integer)
    nome_competicao_fk = Column(String, ForeignKey("competicao.nome_competicao"))

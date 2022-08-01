# api-jogos-olimpicos-fast-api

-- Projeto de Teste elaborado para LuizaLabs para vaga de Desenvolvedor Python, neste projeto foi utilizado Python 3.9.13 com o Framework de back-end Fast API.

-- Este projeto simula um Sistema que calcula e determina vencedores de determinadas provas das Olímpiadas de acordo com algumas regras de negócio definidas previamente.

Siga as instruções abaixo para executar o projeto em sua máquina:
Pré resitos:
- Ter instalado Python 3.9 ou superior;
- Ter instalado o Docker em sua máquina;
- Abrir o Docker Desktop;
Execute no terminal na raiz do projeto e insira os seguintes comandos:
> pip install virtualenv
> source venv/bin/activate
> pip install fastapi uicorn
> docker-compose up --build (somente a primeira vez para baixar as dependencias)
> uvicorn app.main:app --host 0.0.0.0 --port 80 --reload
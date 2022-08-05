# api-jogos-olimpicos-fast-api

-- Projeto de Teste elaborado para a LuizaLabs, para vaga de Desenvolvedor Python, neste projeto foi utilizado Python 3.9.13 com o Framework de back-end Fast API e o SGBD SQLite.

-- Este projeto simula um Sistema que calcula e determina vencedores de determinadas provas das Olímpiadas de acordo com algumas regras de negócio definidas previamente.

Siga as instruções abaixo para executar o projeto em sua máquina:

- Pré requisitos:
- Ter instalado Python 3.9 ou superior;
- Ter instalado o Docker em sua máquina;
- Abrir o Docker Desktop;

Execute no terminal na raiz do projeto e insira os seguintes comandos:

> pip install virtualenv

> source venv/bin/activate

> docker-compose up --build (somente a primeira vez para baixar as dependencias)

> FASTAPI__DATABASE=sqlite:///olimpiadas.db uvicorn app.main:app --host 0.0.0.0 --port 80 --reload

- Após executar os comandos acima, caminhe até o diretório infra/ e execute o arquivo "create_data_base.py" este arquivo criará o banco de dados no SQLite e criará a primeira competição.

- Para acessar os End-Points através do navegador acesse http://0.0.0.0/docs no seu browser e teste os mesmos através da interface do Swagger.

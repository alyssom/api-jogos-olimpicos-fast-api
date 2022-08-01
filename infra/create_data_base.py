import sqlite3

banco = sqlite3.connect('olimpiadas.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE competicao (nome_competicao STRING REFERENCES resultados_competicoes (nome_competicao) PRIMARY KEY, data_inicio DATE NOT NULL, data_encerramento DATE, FOREIGN KEY (nome_competicao) REFERENCES resultados_competicoes (competicao))")
cursor.execute("CREATE TABLE resultados_competicoes (id BIGINT PRIMARY KEY NOT NULL, nome_atleta STRING NOT NULL, unidade STRING NOT NULL, valor DOUBLE NOT NULL, nome_competicao STRING REFERENCES competicao (nome_competicao) NOT NULL, FOREIGN KEY (nome_competicao) REFERENCES competicao (nome_competicao))")

cursor.execute("INSERT INTO competicao VALUES('100m classificatoria 1', '2022/05/13', NULL)")
cursor.execute("INSERT INTO resultados_competicoes VALUES(1, 'Alyssom', 's', 10.234, '100m classificatoria 1')")

banco.commit()

USE lucast;


CREATE TABLE treino(
    id integer not null auto_increment,
    nome_do_exercicio varchar(15),
    dia_da_semana varchar(20),
    carga integer,
    repeticoes integer,
    PRIMARY KEY(id)
);

INSERT INTO treino (nome_do_exercicio, dia_da_semana, carga, repeticoes) VALUES ('Supino Reto', 'Segunda feira', 20, 15);




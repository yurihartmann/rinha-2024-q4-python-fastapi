-- Coloque scripts iniciais aqui
CREATE TABLE clientes (
    id integer primary key,
    nome text,
    limite integer,
    saldo integer default 0
);

CREATE TABLE transacoes (
    uuid varchar(36) primary key,
    id_client integer,
    valor integer,
    tipo char,
    descricao varchar(10),
    realizada_em timestamp
);

INSERT INTO clientes (id, nome, limite)
  VALUES
    (1, 'o barato sai caro', 1000 * 100),
    (2, 'zan corp ltda', 800 * 100),
    (3, 'les cruders', 10000 * 100),
    (4, 'padaria joia de cocaia', 100000 * 100),
    (5, 'kid mais', 5000 * 100);
END;
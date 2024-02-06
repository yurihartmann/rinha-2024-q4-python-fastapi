-- Coloque scripts iniciais aqui
CREATE TABLE clientes (
    id integer primary key,
    limite integer,
    saldo_inicial integer
);

CREATE TABLE transacoes (
    id_client integer,
    valor integer,
    tipo char,
    descricao varchar(10),
    realizada_em DATE
);

DO $$
BEGIN
  INSERT INTO clientes (nome, limite)
  VALUES
    ('o barato sai caro', 1000 * 100),
    ('zan corp ltda', 800 * 100),
    ('les cruders', 10000 * 100),
    ('padaria joia de cocaia', 100000 * 100),
    ('kid mais', 5000 * 100);
END; $$
CREATE TABLE Produto(
    Codigo integer not null,
    CONSTRAINT pk_Codigo_pk PRIMARY KEY (Codigo),
    Nome varchar2(100),
    descricao varchar2(255),
    custo number,
    custo_fixo number,
    comissao number,
    impostos number,
    rentabilidade number
);
INSERT INTO Produto(Codigo, Nome, descricao, custo, custo_fixo, comissao, impostos)
VALUES (1, 'P�o de Hamburguer', 'Massa do P�o tipo Burger - 12 unidades', 46.50, 0.15, 0.05, 0.045)

INSERT INTO Produto(Codigo, Nome, descricao, custo, custo_fixo, comissao, impostos)
VALUES (2, 'P�o Franc�s', '20 p�es franc�s', 2.09, 0.15, 0.05, 0.045)

INSERT INTO Produto(Codigo, Nome, descricao, custo, custo_fixo, comissao, impostos, rentabilidade)
VALUES (3, 'Capuccino', 'Capuccino em p�', 39.75, 0.15, 0.05, 0.045, 10.95)

UPDATE Produto
SET rentabilidade = 0.15
WHERE Codigo = 1

UPDATE Produto
SET rentabilidade = 0.15
WHERE Codigo = 2

UPDATE Produto
SET rentabilidade = 0.15
WHERE Codigo = 3

ALTER TABLE Produto
ADD preco_venda number
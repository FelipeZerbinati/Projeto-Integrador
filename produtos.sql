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
VALUES (1, 'Pão de Hamburguer', 'Massa do Pão tipo Burger - 12 unidades', 46.50, 0.15, 0.05, 0.045)

INSERT INTO Produto(Codigo, Nome, descricao, custo, custo_fixo, comissao, impostos)
VALUES (2, 'Pão Francês', '20 pães francês', 2.09, 0.15, 0.05, 0.045)

INSERT INTO Produto(Codigo, Nome, descricao, custo, custo_fixo, comissao, impostos, rentabilidade)
VALUES (3, 'Capuccino', 'Capuccino em pó', 39.75, 0.15, 0.05, 0.045, 10.95)

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

Update produto
set impostos = 0.18


INSERT INTO Produto(Codigo, Nome, descricao, custo, custo_fixo, comissao, impostos, rentabilidade)
VALUES (4, 'Chocolate', 'Chocolate em barra - 125g', 6.59, 0.15, 0.05, 0.18, 0.15),

INSERT INTO Produto(Codigo, Nome, descricao, custo, custo_fixo, comissao, impostos, rentabilidade)
VALUES (5, 'Pão de Queijo', 'Pão feito com queijo e ovo - porção com 4 pães', 3.5, 0.15, 0.05, 0.18, 0.15),

INSERT INTO Produto(Codigo, Nome, descricao, custo, custo_fixo, comissao, impostos, rentabilidade)
VALUES (6, 'Pão de forma', 'Pão em formato quadrado - 1 pacote', 5, 0.15, 0.05, 0.18, 0.15),

INSERT INTO Produto(Codigo, Nome, descricao, custo, custo_fixo, comissao, impostos, rentabilidade)
VALUES (7, 'Broa de milho', 'Doce feito com milho - 1 unidade', 1.5, 0.15, 0.05, 0.18, 0.15),

INSERT INTO Produto(Codigo, Nome, descricao, custo, custo_fixo, comissao, impostos, rentabilidade)
VALUES (8, 'Rosquinha', 'Rosca doce - 1 unidade', 0.75, 0.15, 0.05, 0.18, 0.15),

INSERT INTO Produto(Codigo, Nome, descricao, custo, custo_fixo, comissao, impostos, rentabilidade)
VALUES (9, 'Bolo', 'Bolo simples - 1 fatia', 3, 0.15, 0.05, 0.18, 0.15),

INSERT INTO Produto(Codigo, Nome, descricao, custo, custo_fixo, comissao, impostos, rentabilidade)
VALUES (10, 'Coxinha de frango', 'Salgado empanado e frito com frango - 1 unidade', 4, 0.15, 0.05, 0.18, 0.15)


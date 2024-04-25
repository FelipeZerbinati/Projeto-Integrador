CREATE TABLE cadastro(
nome_usuario varchar2(255) PRIMARY KEY NOT NULL,
senha varchar2(255) NOT NULL,
email varchar2(255),
num_telefone number
);

ALTER TABLE cadastro
ADD administrador varchar2(3);

ALTER TABLE cadastro
MODIFY administrador varchar2(4);


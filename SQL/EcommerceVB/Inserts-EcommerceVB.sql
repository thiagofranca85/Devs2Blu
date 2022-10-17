-- Inserindo dados EcommerceVB
-- Inserindo valores na tabela cliente.
begin transaction;

insert into cliente (nome, cpf, email)
values ('Thiago', '6549873514', 'thiago@vb.com');

insert into cliente (nome, cpf, email)
values ('Gisele', '7546546465', 'gisele@vb.com');

insert into cliente (nome, cpf, email)
values ('Vander', '9654654321', 'vander@vb.com');

commit;
end;
-- Inserindo valores na tabela filial.
begin transaction;

insert into filial (nome) values ('VB Blumenau');

commit;
end;
-- Inserindo valores na tabela funcionario.
begin transaction;

insert into funcionario (nome, cpf, admissao, id_filial)
values ('Thiago', '6549873514', '2022-10-14', 1);

insert into funcionario (nome, cpf, admissao, id_filial)
values ('Gisele', '7546546465', '2022-10-14', 1);

insert into funcionario (nome, cpf, admissao, id_filial)
values ('Vander', '9654654321', '2022-10-14', 1);

commit;
end;
-- Inserindo produtos na tabela item.
begin transaction;

insert into item (produto,tipo,valor)
values ('Torneira Monocomando','metais',559.00);

insert into item (produto,tipo,valor)
values ('Tapete para banheiro','banho',59.00);

insert into item (produto,tipo,valor)
values ('Toalha de banho','banho',89.00);

insert into item (produto,tipo,valor)
values ('Toalheiro banheiro','banho',129.00);

insert into item (produto,tipo,valor)
values ('Escorredor de pratos','mesa',49.00);

insert into item (produto,tipo,valor)
values ('toalha de louca','mesa',29.00);

insert into item (produto,tipo,valor)
values ('lencol queen','cama',69.00);

insert into item (produto,tipo,valor)
values ('fronha travesseiro','cama',39.00);

commit;
end;
-- Inserindo compras na tabela compras.
begin transaction;

insert into compra (endereco_entrega,data_compra,cod_cli,cod_fun,cod_item)
values ('Rua da Matriz, 785, Centro, Itapiranga-SC','2022-10-02',1,3,7);

insert into compra (endereco_entrega,data_compra,cod_cli,cod_fun,cod_item)
values ('Rua Max Hering, 184, Victor Konder, Blumenau-SC','2022-10-04',3,1,6);

insert into compra (endereco_entrega,data_compra,cod_cli,cod_fun,cod_item)
values ('Rua Sete de Setembro, 1000, Centro, Blumenau-SC','2022-10-05',2,2,4);

insert into compra (endereco_entrega,data_compra,cod_cli,cod_fun,cod_item)
values ('Rua Max Hering, 184, Victor Konder, Blumenau-SC','2022-10-06',3,2,1);

insert into compra (endereco_entrega,data_compra,cod_cli,cod_fun,cod_item)
values ('Rua Sete de Setembro, 1000, Centro, Blumenau-SC','2022-10-08',2,1,3);

insert into compra (endereco_entrega,data_compra,cod_cli,cod_fun,cod_item)
values ('Rua da Matriz, 785, Centro, Itapiranga-SC','2022-10-08',1,2,2);

insert into compra (endereco_entrega,data_compra,cod_cli,cod_fun,cod_item)
values ('Rua Sete de Setembro, 1000, Centro, Blumenau-SC','2022-10-10',2,3,8);

commit;
end;


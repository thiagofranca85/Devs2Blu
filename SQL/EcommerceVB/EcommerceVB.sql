-- Criando tabelas EcommerceVB
-- pessoa vai herdar para cliente e funcionario

-- Tabela pessoa
begin transaction;

create table pessoa (
	 nome varchar (60) not null
	,cpf varchar (14) not null unique
);

-- Tabela cliente
create table cliente (
	 cod_cli int generated always as identity primary key
	,email varchar (60) not null
) inherits (pessoa);

-- Tabela filial
create table filial (
	 cod_filial int generated always as identity primary key
	,nome varchar (30) not null
);

-- Tabela funcionario
create table funcionario (
	 cod_fun int generated always as identity primary key
	,admissao date not null
	,demissao date null
	,id_filial int
) inherits (pessoa);

-- Tabela item
create table item (
	 cod_item int generated always as identity primary key
	,produto varchar (30) not null
	,tipo varchar (30) not null
	,valor decimal (7,2) not null
);


-- Tabela compra (Conexao com cliente e funcionario)
create table compra (
	 cod_compra int generated always as identity primary key
	,endereco_entrega varchar (60) not null
	,data_compra date not null
	,cod_cli int
	,cod_fun int
	,cod_item int
);

-- Fazendo as alterações e adicionando as FK (Foreign Keys) após criar as tabelas
alter table funcionario add constraint id_filial foreign key (id_filial) references filial(cod_filial);
alter table compra add constraint cod_cli foreign key (cod_cli) references cliente (cod_cli);
alter table compra add constraint cod_fun foreign key (cod_fun) references funcionario (cod_fun);
alter table compra add constraint cod_item foreign key (cod_item) references item (cod_item);

commit;
end;


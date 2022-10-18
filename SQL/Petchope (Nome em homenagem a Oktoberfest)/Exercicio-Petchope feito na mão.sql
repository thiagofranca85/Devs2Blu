-- Parte 1 - Criar a tabela pessoa
begin transaction;
create table pessoa(
	 id int generated always as identity primary key
	,nome varchar(70) not null
	,idade int not null
	,email varchar(40) not null
	,cpf varchar(11) not null
);
commit;
end;

-- Parte 2 - Criar cliene e funcionario com Foreign key
begin transaction;
create table cliente(
	 id int generated always as identity primary key
	,telefone int not null
	,id_pessoa int
	,foreign key (id_pessoa) references pessoa(id)
);

create table funcionario(
	 id int generated always as identity primary key
	,funcao varchar(30) not null
	,admissao date not null
	,demissao date null
	,id_pessoa int
	,foreign key (id_pessoa) references pessoa(id)
);
commit;
end;

-- Parte 3 - Criar a tabela especie
begin transaction;
create table especie(
	 id int generated always as identity primary key
	,descricao varchar(40) not null
);
commit;
end;

-- Parte 4 - Criar a tabela de Pet
begin transaction;
create table pet(
	 id int generated always as identity primary key
	,nome varchar(40) not null
	,raca varchar(40) not null
	,peso decimal(5,2) not null
	,idade int not null
	,sexo boolean not null
	,id_cliente int
	,foreign key (id_cliente) references cliente(id)
	,idpet_especie int
	,foreign key (idpet_especie) references especie(id)
);
commit;
end;

-- Parte 5 - Criar tabela de servi�os
begin transaction;
create table servico(
	 id int generated always as identity primary key
	,descricao varchar(50) not null
	,valor decimal(7,2) not null
);
commit;
end;

-- Parte 6 - Criar tabela agendamento
begin transaction;
create table agendamento(
	 id int generated always as identity primary key
	,data_agendamento date not null
	,hora_agen_inicial time not null
	,hora_agen_final time not null
	,checkin time not null
	,checkout time not null
	,id_pet int
	,foreign key (id_pet) references pet(id)
	,id_servico int
	,foreign key (id_servico) references servico(id)
	,id_funcionario int
	,foreign key (id_funcionario) references funcionario(id)
);
commit;
end;

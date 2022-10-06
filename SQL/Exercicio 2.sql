-- DQL
-- Criar tabela funcionarios
create table funcionarios (
	 id int generated always as identity
	,nome varchar(30) not null
	,sobrenome varchar(30) not null
	,idade int null
);

-- Adicionar 20 funcionarios na planilha
insert into funcionarios (nome,sobrenome,idade)values('Thiago','Lirinha',36);
insert into funcionarios (nome,sobrenome,idade)values('Joao','Lirinha',25);
insert into funcionarios (nome,sobrenome,idade)values('Vander','Lirinha',17);
insert into funcionarios (nome,sobrenome,idade)values('Dieter','Lirinha',30);
insert into funcionarios (nome,sobrenome,idade)values('Luiza','Bissoni',28);
insert into funcionarios (nome,sobrenome,idade)values('Haiko','Ruediger',25);
insert into funcionarios (nome,sobrenome,idade)values('Joao','Victor',18);
insert into funcionarios (nome,sobrenome,idade)values('Everton','Denega',36);
insert into funcionarios (nome,sobrenome,idade)values('Larissa','Hoffmann',36);
insert into funcionarios (nome,sobrenome,idade)values('Jean','Niehues',42);
insert into funcionarios (nome,sobrenome,idade)values('Marco','Silva',23);
insert into funcionarios (nome,sobrenome,idade)values('Lucas','Silva',25);
insert into funcionarios (nome,sobrenome,idade)values('Nicolas','Lirinha',19);
insert into funcionarios (nome,sobrenome,idade)values('Melissa','Konig',27);
insert into funcionarios (nome,sobrenome,idade)values('Bruno','Baccin',26);
insert into funcionarios (nome,sobrenome,idade)values('Gisele','Silva',23);
insert into funcionarios (nome,sobrenome,idade)values('Guilherme','Wanser',28);
insert into funcionarios (nome,sobrenome,idade)values('Marcio','Lourenço',27);
insert into funcionarios (nome,sobrenome,idade)values('Felipe','Weiss',25);
insert into funcionarios (nome,sobrenome,idade)values('Alejandro','Silveira',23);

-- Busca funcionarios com sobrenome Lirinha
select * from funcionarios where sobrenome  = 'Lirinha';

-- Alterar sobrenome lirinha para o nome correto
update funcionarios set sobrenome = 'França' where id = 1;
update funcionarios set sobrenome = 'Casali' where id = 2;
update funcionarios set sobrenome = 'Lauschner' where id = 3;
update funcionarios set sobrenome = 'Heiss' where id = 4;
update funcionarios set sobrenome = 'Boladao' where id = 13;

-- Faça uma busca por nomes que contem a letra A no inicio
select * from funcionarios where nome like 'A%'

-- Faça uma busca por nomes que contem a letra A no inicio e idade > 18
select * from funcionarios where nome like 'A%' and idade > 18

-- Deletar usuario com letra A e maior que 18
delete from funcionarios where id = 20

-- Modificar posicao da coluna
alter table funcionarios 
	modify column idade after nome
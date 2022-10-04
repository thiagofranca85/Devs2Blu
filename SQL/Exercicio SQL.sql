-- Criar Tabela
create table pessoas (
	 id int generated always as identity
	,nome varchar(30) not null
	,sobrenome varchar(30) not null
	,idade int null
);

-- Adicionar CPF
alter table pessoas 
add cpf varchar(11) not null default '00000000000'

-- Deletar Coluna Idade
alter table pessoas 
drop column idade

-- Alterar nome da Tabela
alter table pessoas rename to funcionario;

-- Adicione uma nova coluna chamada Salario
alter table funcionario 
add salario float not null default 1800

-- Inserir 4 novos funcionarios
insert into funcionario (nome,sobrenome,cpf,salario)
values('Larissa','Hoffmann','12365478945',1900)

-- Faça update de salario de 5 funcionários // Usando conceito de operadores relacionais
update funcionario set salario = 2000
where id >= 1 and id <= 6

-- Apenas Curiosidade alterar todos que tem um valor especifico por outro
update funcionario set salario = 1700
	where salario = 1900
	
-- Adicionar coluna idade que permite dados nulos
alter table funcionario
add idade int null

-- Deletar 3 funcionarios pelo ID
delete from funcionario where id = 5
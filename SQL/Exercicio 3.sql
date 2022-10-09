begin transaction;

	create table pessoas(
		 id int not null generated always as identity
		,nome varchar (20) not null
		,sobrenome varchar (30) not null
		,idade int not null
		,cpf varchar (14)
	);
	
	create table funcionario(
		 id int not null generated always as identity
		,cargo varchar (20) not null
		,setor varchar (30) not null
		,salario int not null
	);
	
commit;
end;

begin transaction;

	insert into pessoas(nome,sobrenome,idade,cpf)
	values('Vander','Silva',20,'00000000000');
	
	-- Salvou um ponto dentro do codigo
	savepoint inserindo_nome;
	
	insert into pessoas(nome,sobrenome,idade,cpf)
	values('Lirinha','Boladao',18,'00000000000');
	
	-- O que estiver entre o savepoint e o rollback sera ignorado
	-- Retorna ao savepoint
	rollback to inserindo_nome;
	
	insert into pessoas(nome,sobrenome,idade,cpf)
	values('Joaozinho','Pereira',20,'00000000000');
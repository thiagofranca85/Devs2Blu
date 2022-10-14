begin transaction;

insert into pessoa (nome,cpf,email)
values('Vander Lauschner',03281099912,'vanderlaus@hotmail.com');

insert into pessoa (nome,cpf,email)
values('Gisele Silva',03281099914,'giselesilva@gmail.com');

insert into pessoa (nome,cpf,email)
values('Thiago Franca',03281099915,'thiagofranca@gmail.com');

commit;
end;

begin transaction;

insert into funcionario (id_pessoa,funcao,admissao)
values(1,'petshop','2022-04-15');

insert into funcionario (id_pessoa,funcao,admissao)
values(2,'petgirl','2022-03-15');

insert into funcionario (id_pessoa,funcao,admissao)
values(3,'petshop2','2022-01-15');

commit;
end;

begin transaction;

insert into cliente (id_pessoa,idade,telefone)
values(1,'41','47991158800');

insert into cliente (id_pessoa,idade,telefone)
values(2,'28','47991168800');

insert into cliente (id_pessoa,idade,telefone)
values(3,'31','4799254850');

commit;
end;

begin transaction;

insert into especie (descricao)
values('cachorro');

insert into especie (descricao)
values('gato');

commit;
end;

begin transaction;

insert into pet (id_cliente,id_especie,nome,raca,peso,idade,sexo)
values(2,1,'Thor','Shitzu',11,9,true);

insert into pet (id_cliente,id_especie,nome,raca,peso,idade,sexo)
values(3,2,'Flokinho','vira lata',4,1,true);

insert into pet (id_cliente,id_especie,nome,raca,peso,idade,sexo)
values(3,2,'Peter','vira lata',3,1,true);

insert into pet (id_cliente,id_especie,nome,raca,peso,idade,sexo)
values(3,2,'Thomas','vira lata',2,3,true);

insert into pet (id_cliente,id_especie,nome,raca,peso,idade,sexo)
values(4,2,'Chico','Siames',5,7,true);

commit;
end;

begin transaction;

insert into servico (descricao,valor)
values('banho',40.00);

insert into servico (descricao,valor)
values('tosa',40.00);

insert into servico (descricao,valor)
values('combo',70.00);

commit;
end;

begin transaction;

insert into agendamento (data_agendamento,hora_dispinicial ,checkin,checkout,id_pet,id_servico,id_funcionario)
values('2022-10-15','14:00:00','14:05:00','14:55:00',1,3,5);

insert into agendamento (data_agendamento,hora_dispinicial,checkin,checkout,id_pet,id_servico,id_funcionario)
values('2022-10-18','15:00:00','15:15:00','16:15:00',3,1,4);

insert into agendamento (data_agendamento,hora_dispinicial,checkin,checkout,id_pet,id_servico,id_funcionario)
values('2022-10-20','16:00:00','16:10:00','16:55:00',5,2,3);

commit;
end;
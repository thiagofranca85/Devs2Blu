begin transaction;

insert into pessoa (nome,idade,email,cpf)
values('Vander Lauschner',41,'vanderlaus@hotmail.com',03281099912);

insert into pessoa (nome,idade,email,cpf)
values('Gisele Silva',25,'giselesilva@gmail.com',03281099914);

insert into pessoa (nome,idade,email,cpf)
values('Thiago Franca',36,'thiagofranca@gmail.com',03281099915);

commit;
end;

begin transaction;

insert into funcionario (id_pessoa,funcao,admissao)
values(1,'Funcionario','2022-04-15');

insert into funcionario (id_pessoa,funcao,admissao)
values(2,'Funcionario','2022-03-15');

insert into funcionario (id_pessoa,funcao,admissao)
values(3,'Funcionario','2022-01-15');

commit;
end;

begin transaction;

insert into cliente (id_pessoa,telefone)
values(1,33223344);

insert into cliente (id_pessoa,telefone)
values(2,33223344);

insert into cliente (id_pessoa,telefone)
values(3,33233444);

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

insert into pet (nome,raca,peso,idade,sexo,id_cliente,idpet_especie)
values('Thor','Shitzu',8,6,true,1,1);

insert into pet (nome,raca,peso,idade,sexo,id_cliente,idpet_especie)
values('Chico','Siames',6,4,true,2,2);

insert into pet (nome,raca,peso,idade,sexo,id_cliente,idpet_especie)
values('Belinha','Viralata',8,6,true,3,1);

insert into pet (nome,raca,peso,idade,sexo,id_cliente,idpet_especie)
values('Theo','Persa',12,6,true,3,2);


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

insert into agendamento (data_agendamento,hora_agen_inicial,hora_agen_final,checkin,checkout,id_pet,id_servico,id_funcionario)
values('2022-10-15','14:00:00','14:05:00','14:06:00','15:00:00',1,3,1);

insert into agendamento (data_agendamento,hora_agen_inicial,hora_agen_final,checkin,checkout,id_pet,id_servico,id_funcionario)
values('2022-10-15','15:00:00','15:05:00','16:06:00','16:00:00',2,2,2);

insert into agendamento (data_agendamento,hora_agen_inicial,hora_agen_final,checkin,checkout,id_pet,id_servico,id_funcionario)
values('2022-10-15','12:00:00','12:05:00','13:06:00','13:00:00',3,2,3);

insert into agendamento (data_agendamento,hora_agen_inicial,hora_agen_final,checkin,checkout,id_pet,id_servico,id_funcionario)
values('2022-10-15','16:00:00','16:05:00','16:06:00','17:00:00',4,1,1);

commit;
end;
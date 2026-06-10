use ctbraga;
 create table pessoas(
 IDpessoa int auto_increment primary key,
 nome varchar(100) not null,
 data_nascimento date not null
 );
create table planos(
 IDplano int auto_increment primary key,
 nome varchar(50) not null,
 valor_plano decimal(10,2) not null,
 duracao_meses int not null,
 qtd_pessoas int not null
 ); 
 create table modalidades(
 IDmodalidade int auto_increment primary key,
 nome varchar(20) not null,
 descricao text
 ); 
 create table cts(
 IDct int auto_increment primary key,
 nome varchar(100) not null
 );
 
 create table telefones(
 IDtelefone int auto_increment primary key,
 numero varchar(20) not null,
 pessoaID int not null,
 foreign key(pessoaID) references pessoas(IDpessoa)
 );
 create table alunos(
 IDaluno int auto_increment primary key,
 status varchar(20) not null,
 pessoaID int unique not null,
 foreign key(pessoaID) references pessoas(IDpessoa)
 );
 create table enderecos(
 IDendereco int auto_increment primary key,
 ctID int  unique not null,
 foreign key(ctID) references cts(IDct),
 rua varchar(150) not null,
 numero varchar(10) not null,
 bairro varchar(150) not null,
 cidade varchar(150) not null,
 uf varchar(2) not null,
 cep varchar(9) not null
 );

create table horarios(
 IDhorario int auto_increment primary key,
 dia_semana varchar(20) not null,
 hora_inicio time not null,
 hora_fim time not null,
 descricao text,
 modalidadeID int not null,
 foreign key(modalidadeID) references modalidades(IDmodalidade),
 ctID int not null,
 foreign key(ctID) references cts(IDct)
 ); 
 
 create table responsabilidades(
 IDresponsabilidade int auto_increment primary key,
 responsavelID int not null,
 foreign key(responsavelID) references pessoas(IDpessoa),
 alunoID int not null,
 foreign key(alunoID) references alunos(IDaluno),
 tipo_responsabilidade varchar(50) not null,
 
 unique(alunoID, responsavelID, tipo_responsabilidade)
 );
 create table matriculas(
 IDmatriculas int auto_increment primary key,
 status_m varchar(20) not null,
 data_inicio date not null,
 data_fim date,
 alunoID int not null,
 foreign key(alunoID) references alunos(IDaluno),
 planoID int not null,
 foreign key(planoID) references planos(IDplano)
 );
 
 create table pagamentos(
 IDpagamento int auto_increment primary key,
 valor_pag decimal(10,2) not null,
 vencimento date not null,
 data_pagamento date,
 status_pag varchar(20) not null,
 matriculaID int not null,
 foreign key(matriculaID) references matriculas(IDmatriculas)
 );
 create table presencas(
 IDpresenca int auto_increment primary key,
 data_presenca date not null,
 alunoID int  not null,
 foreign key(alunoID) references alunos(IDaluno),
 horarioID int not null,
 foreign key(horarioID) references horarios(IDhorario),
 
 unique(horarioID, alunoID, data_presenca)
 );
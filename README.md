# CT Braga System

Sistema de gerenciamento para centros de treinamento, desenvolvido em Python com persistência em banco de dados MariaDB.

O projeto tem como objetivo aplicar conceitos de desenvolvimento de software, modelagem de banco de dados, programação orientada a objetos, SQL e boas práticas de programação, simulando um sistema real utilizado para administração de alunos, responsáveis, mensalidades e demais processos administrativos de um centro de treinamento.

---

## Funcionalidades Implementadas

### Módulo de Alunos

* Cadastro de alunos
* Listagem de alunos
* Alteração de dados cadastrais
* Remoção de alunos
* Persistência completa em banco de dados MariaDB

### Banco de Dados

* Modelagem relacional normalizada
* Relacionamento entre pessoas, alunos e telefones
* Utilização de chaves primárias e estrangeiras
* Operações CRUD utilizando SQL
* Persistência de dados em MariaDB

---

## Funcionalidades em Desenvolvimento

### Módulo de Responsabilidades

Regras de negócio definidas:

* Um aluno pode possuir vários responsáveis legais
* Um aluno pode possuir apenas um responsável financeiro
* Uma pessoa pode ser responsável por vários alunos
* Uma mesma pessoa pode ser responsável legal e financeiro do mesmo aluno
* Não são permitidas responsabilidades duplicadas

### Funcionalidades Futuras

* Controle de mensalidades
* Controle de modalidades
* Controle de turmas
* Relatórios administrativos
* API para integração com frontend
* Interface gráfica/Web

---

## Tecnologias Utilizadas

* Python 3
* MariaDB
* MySQL Connector
* SQL
* Git
* GitHub

---

## Estrutura Atual do Projeto

```text
ctbraga_system/
│
├── database/
│   ├── conexao.py
│   └── teste_conexao.py
│
├── modules/
│   ├── alunos.py
│   └── responsabilidades.py
│
├── ctbraga_sql/
│   ├── ctbraga_system_DER.mwb
│   ├── diagrama.sql
│   └── script_ctbraga.sql
│
├── data/
│   └── DER/
│
├── main.py
├── README.md
└── .gitignore
```

---

## Objetivos do Projeto

Este projeto está sendo desenvolvido como ferramenta de aprendizado e evolução profissional, com foco em:

* Desenvolvimento Backend
* Banco de Dados Relacional
* Modelagem de Sistemas
* Boas Práticas de Programação
* Controle de Versão com Git
* Construção de Projetos para Portfólio

---

## Evolução do Projeto

O CT Braga System está sendo desenvolvido de forma incremental, seguindo uma abordagem de aprendizado prático e evolução contínua.

### Principais etapas já concluídas

#### Versão Inicial

* Estrutura básica do projeto criada em Python
* CRUD de alunos utilizando listas em memória
* Implementação das primeiras validações de entrada

#### Migração para Banco de Dados

* Modelagem completa do banco de dados
* Criação do DER (Diagrama Entidade-Relacionamento)
* Implementação do banco MariaDB
* Criação das tabelas e relacionamentos
* Migração gradual do CRUD para persistência em banco

#### Refatorações

* Separação do código em módulos
* Reutilização de funções de validação
* Padronização das operações CRUD
* Eliminação gradual da lógica baseada em listas
* Implementação de consultas SQL com JOINs

#### Versão Atual

* Módulo de alunos totalmente integrado ao banco de dados
* Cadastro, listagem, alteração e remoção funcionando
* Estrutura preparada para expansão dos demais módulos
* Desenvolvimento do módulo de responsabilidades em andamento

### Próximas Etapas

* Implementação completa do módulo de responsabilidades
* Controle de mensalidades
* Controle de modalidades e turmas
* Implementação de API
* Desenvolvimento do frontend
* Evolução para uma arquitetura mais próxima de sistemas profissionais

### Aprendizados Aplicados

Durante o desenvolvimento do projeto estão sendo praticados conceitos como:

* Modelagem de banco de dados relacional
* SQL e relacionamentos entre tabelas
* Programação modular
* Refatoração de código
* Tratamento de exceções
* Controle de versão com Git e GitHub
* Organização de projetos reais
* Regras de negócio e modelagem de domínio
* Evolução incremental de software

---

## Status do Projeto

**Versão atual:** v0.3.0

Projeto em desenvolvimento ativo.

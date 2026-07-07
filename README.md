# TechFlow Task Manager

Sistema web de gerenciamento de tarefas desenvolvido pela **TechFlow Solutions**
para uma startup de logística, com o objetivo de permitir o acompanhamento do
fluxo de trabalho em tempo real, priorização de tarefas críticas e
monitoramento do desempenho da equipe.

Este repositório é o produto de um trabalho acadêmico da disciplina de
Engenharia de Software, simulando o ciclo de vida completo de um projeto ágil:
planejamento, desenvolvimento, controle de qualidade e gestão de mudanças.

## Objetivo do projeto

Fornecer um sistema simples e funcional em que cada usuário possa:

- Criar uma conta e autenticar-se de forma segura (senhas com hash);
- Cadastrar, visualizar, atualizar e excluir suas próprias tarefas (CRUD);
- Organizar as tarefas em um quadro estilo Kanban com três status:
  **A Fazer**, **Em Progresso** e **Concluído**.

## Escopo inicial

O escopo inicial do projeto contempla:

- Cadastro e login de usuários;
- CRUD de tarefas vinculado ao usuário autenticado;
- Visualização das tarefas em formato de quadro Kanban;
- Testes automatizados cobrindo autenticação e CRUD;
- Pipeline de integração contínua (GitHub Actions) validando qualidade de
  código e execução dos testes a cada alteração.

> A seção [Gestão de Mudanças](#gestão-de-mudanças) documenta uma alteração de
> escopo simulada, feita após a entrega da versão inicial.

## Metodologia adotada

O desenvolvimento seguiu uma abordagem **Kanban**, com o fluxo de trabalho
organizado no GitHub Projects em três colunas (**To Do**, **In Progress**,
**Done**). Cada funcionalidade foi tratada como um cartão individual, movido
entre as colunas conforme o progresso, e implementada em commits pequenos e
descritivos — favorecendo entrega contínua e rastreabilidade das mudanças, em
vez de sprints com prazos fixos (como no Scrum).

## Estrutura do repositório

```
techflow-task-manager/
├── .github/workflows/ci.yml   # Pipeline de CI (testes + lint)
├── src/                       # Código-fonte da aplicação Flask
│   ├── routes/                 # Blueprints (auth, tasks)
│   ├── templates/              # Views HTML (Jinja2)
│   ├── static/                 # CSS
│   ├── __init__.py             # Application factory
│   ├── config.py               # Configurações (dev/test)
│   └── models.py               # Modelos (User, Task)
├── tests/                     # Testes automatizados (Pytest)
├── docs/                      # Diagramas UML e demais documentos
├── requirements.txt
├── pytest.ini
├── setup.cfg                  # Configuração do flake8
└── run.py                     # Ponto de entrada da aplicação
```

## Como executar o sistema

Pré-requisitos: Python 3.11+.

```bash
# 1. Clonar o repositório
git clone https://github.com/<seu-usuario>/techflow-task-manager.git
cd techflow-task-manager

# 2. Criar e ativar um ambiente virtual
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Linux/Mac

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Rodar a aplicação
python run.py
```

A aplicação sobe em `http://127.0.0.1:5000`. Crie uma conta em `/register` e
faça login para acessar o quadro de tarefas.

## Testes automatizados

Os testes usam **Pytest** e o cliente de testes do Flask, cobrindo:

- Cadastro, login, logout e validação de credenciais;
- Criação, atualização de status, exclusão e validação de entrada das tarefas;
- Isolamento de dados entre usuários diferentes.

Para rodar localmente:

```bash
pip install -r requirements.txt
pytest -v
```

## Controle de qualidade (CI)

O workflow em [`.github/workflows/ci.yml`](.github/workflows/ci.yml) é
executado automaticamente a cada `push`/`pull request` na branch `main` e
realiza duas verificações:

1. **Lint** com `flake8`, garantindo padronização do código;
2. **Testes automatizados** com `pytest`.

## Gestão de Mudanças

_(Esta seção será atualizada com a justificativa da mudança de escopo
simulada, conforme descrito na tarefa de Gestão de Mudanças do trabalho.)_

## Quadro Kanban

O planejamento e acompanhamento das tarefas está disponível na aba
[Projects](../../projects) deste repositório, organizado nas colunas **To
Do**, **In Progress** e **Done**.

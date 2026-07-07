# TechFlow Task Manager

Sistema web de gerenciamento de tarefas desenvolvido pela TechFlow Solutions
para uma startup de logística. A ideia é permitir que a equipe acompanhe o
fluxo de trabalho em tempo real, priorize tarefas críticas e monitore o
andamento das atividades.

Este repositório é o trabalho prático da disciplina de Engenharia de
Software, simulando o ciclo de vida de um projeto ágil: planejamento,
desenvolvimento, controle de qualidade e gestão de mudanças.

## Objetivo do projeto

Cada usuário pode criar uma conta, autenticar-se de forma segura (senha
armazenada com hash) e gerenciar suas próprias tarefas: criar, visualizar,
atualizar e excluir (CRUD), organizando tudo em um quadro estilo Kanban com
três colunas — A Fazer, Em Progresso e Concluído.

## Escopo inicial

A primeira versão do projeto contempla:

- Cadastro e login de usuários
- CRUD de tarefas vinculado ao usuário autenticado
- Quadro Kanban para visualização das tarefas
- Testes automatizados cobrindo autenticação e CRUD
- Pipeline de integração contínua (GitHub Actions) validando qualidade de
  código e execução dos testes a cada alteração

A seção [Gestão de Mudanças](#gestão-de-mudanças) mais abaixo conta como esse
escopo foi ampliado depois da entrega inicial.

## Metodologia adotada

O desenvolvimento seguiu Kanban, com o fluxo de trabalho organizado no
GitHub Projects em três colunas (To Do, In Progress, Done). Cada
funcionalidade virou um cartão, movido entre as colunas conforme o
progresso, e implementada em commits pequenos e descritivos. A escolha por
Kanban em vez de Scrum foi por não fazer sentido dividir um projeto desse
tamanho em sprints com prazos fixos — o fluxo contínuo de cartões representa
melhor o ritmo real do desenvolvimento.

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
git clone https://github.com/TiagoPeixe-Dev/techflow-task-manager.git
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

A aplicação sobe em http://127.0.0.1:5000. Crie uma conta na tela de
cadastro e faça login para acessar o quadro de tarefas.

## Testes automatizados

Os testes usam Pytest e o cliente de testes do Flask, cobrindo cadastro,
login, logout e validação de credenciais, além de criação, atualização de
status, exclusão e validação de entrada das tarefas, e o isolamento de dados
entre usuários diferentes.

Para rodar localmente:

```bash
pip install -r requirements.txt
pytest -v
```

## Controle de qualidade (CI)

O workflow definido em [.github/workflows/ci.yml](.github/workflows/ci.yml)
roda automaticamente a cada push ou pull request na branch principal,
verificando padronização do código com flake8 e executando a suíte de
testes com pytest.

## Gestão de Mudanças

Depois da primeira versão do CRUD já funcionando, adicionamos um campo de
prioridade às tarefas (baixa, media, alta, critica). O quadro passou a
ordenar as tarefas da mais crítica para a menos crítica e cada card ganhou
um indicador visual colorido de acordo com a prioridade.

Essa mudança não estava no escopo original, mas fazia falta: o desafio da
TechFlow Solutions pede explicitamente que o sistema ajude a priorizar
tarefas críticas, e a primeira versão só tinha título, descrição e status —
não havia como sinalizar que uma tarefa era mais urgente que outra. Sem
esse campo, o sistema não cumpria de verdade um dos objetivos que o cliente
pediu.

O card "Implementar mudança de escopo: prioridade das tarefas" já existia
no backlog do Kanban antes de começarmos a implementação, foi movido para
In Progress durante o desenvolvimento e passou por um commit dedicado,
cobrindo modelo, rotas, template, estilo visual e testes. Só foi para Done
depois que o CI passou. Isso é meio o ponto de trabalhar com Kanban: uma
mudança de escopo entra como mais um item do backlog e segue o mesmo fluxo
de qualquer outra tarefa, sem precisar renegociar um sprint inteiro.

## Quadro Kanban

O planejamento e acompanhamento das tarefas está na aba
[Projects](../../projects) deste repositório, organizado nas colunas To Do,
In Progress e Done.

# Parte Teórica — Construindo um Projeto Ágil no GitHub: Da Gestão ao Controle de Qualidade

**Projeto:** TechFlow Task Manager
**Repositório:** https://github.com/TiagoPeixe-Dev/techflow-task-manager
**Autor:** Tiago Antunes Peixe

> Este documento é um rascunho pronto para ser copiado para Word/Google Docs,
> complementado com os prints solicitados, e exportado como PDF/DOCX para
> entrega. Os diagramas UML estão em `docs/diagrama-casos-de-uso.md` e
> `docs/diagrama-classes.md` — renderize-os em https://mermaid.live e cole as
> imagens exportadas nos locais indicados abaixo.

---

## 1. Descrição do projeto e escopo inicial

A **TechFlow Solutions**, empresa fictícia especializada em soluções de
software, foi contratada por uma startup de logística para desenvolver um
sistema de gerenciamento de tarefas baseado em metodologias ágeis. O
objetivo é permitir que a equipe acompanhe o fluxo de trabalho em tempo
real, priorize tarefas críticas e monitore o andamento das atividades.

O **escopo inicial** definido para a primeira entrega contemplou:

- Cadastro e autenticação de usuários (login/logout), com senhas protegidas
  por hash;
- CRUD de tarefas (criar, listar, atualizar status, excluir), vinculado a
  cada usuário autenticado;
- Visualização das tarefas em um quadro estilo Kanban com três colunas:
  **A Fazer**, **Em Progresso** e **Concluído**;
- Testes automatizados cobrindo autenticação e CRUD;
- Pipeline de integração contínua (GitHub Actions) validando qualidade de
  código e execução dos testes a cada alteração no repositório.

Esse escopo foi posteriormente ampliado por uma mudança de escopo formal,
detalhada na Seção 5 deste documento.

## 2. Metodologia ágil utilizada

O projeto foi conduzido com uma abordagem **Kanban**, escolhida por três
motivos principais:

1. O trabalho é de fluxo contínuo (tarefas de configuração, implementação,
   testes e documentação intercaladas), sem a necessidade de sprints com
   duração fixa, como no Scrum;
2. O GitHub Projects oferece suporte nativo a quadros Kanban, integrados a
   issues/commits do próprio repositório, o que reduz o atrito entre
   planejamento e execução;
3. Kanban favorece a visibilidade do trabalho em andamento (WIP) e facilita
   a incorporação de mudanças de escopo a qualquer momento — como aconteceu
   neste projeto — sem romper um ciclo de sprint já em andamento.

O fluxo de trabalho foi organizado em três colunas — **To Do**, **In
Progress** e **Done** — refletindo, cartão a cartão, cada etapa do
desenvolvimento (desde a estruturação do repositório até a gravação do
vídeo final). Cada cartão corresponde a uma unidade de trabalho que gerou
um ou mais commits descritivos no repositório.

## 3. Importância da modelagem em Engenharia de Software

Modelar um sistema antes (ou durante) sua implementação — por meio de
diagramas UML, por exemplo — cumpre um papel que vai além da documentação:

- **Comunicação**: um diagrama de classes ou de casos de uso comunica a
  estrutura e o comportamento do sistema a outros desenvolvedores, ao
  cliente ou a um revisor de código, de forma muito mais rápida do que a
  leitura do código-fonte completo;
- **Antecipação de problemas**: ao desenhar o relacionamento entre `User` e
  `Task`, por exemplo, fica evidente que toda tarefa precisa pertencer a um
  usuário — o que orienta decisões de implementação (chave estrangeira,
  regra de autorização) antes mesmo de escrever a primeira linha de código;
- **Base para mudanças**: quando o escopo muda (como ocorreu neste projeto,
  com a adição do campo de prioridade), ter um modelo de classes já
  existente facilita identificar exatamente onde a mudança deve ser
  aplicada e quais partes do sistema são impactadas;
- **Redução de ambiguidade**: requisitos descritos apenas em texto (como o
  desafio original) são naturalmente ambíguos; um diagrama de casos de uso
  força a explicitação de quem interage com o sistema e o que exatamente
  cada interação faz.

Por esses motivos, a modelagem foi tratada neste projeto não como uma
formalidade acadêmica isolada, mas como uma ferramenta de apoio direto às
decisões de implementação.

## 4. Diagramas UML

### 4.1. Diagrama de Casos de Uso

_(Inserir aqui a imagem exportada de `docs/diagrama-casos-de-uso.md`.)_

O ator único do sistema é o **Usuário**, que pode se cadastrar, autenticar-se
e realizar as operações de CRUD sobre suas próprias tarefas, incluindo a
atualização de status (posição no Kanban) e de prioridade.

### 4.2. Diagrama de Classes

_(Inserir aqui a imagem exportada de `docs/diagrama-classes.md`.)_

O modelo é composto por duas classes persistentes — `User` e `Task` — em
relação um-para-muitos, e duas enumerações de valores válidos (`status` e
`priority`), validadas na camada de rotas antes da persistência.

## 5. Gestão de Mudanças: justificativa da mudança de escopo

**Mudança realizada:** adição de um campo de **prioridade** (`baixa`,
`media`, `alta`, `critica`) às tarefas, com reordenação automática do quadro
pela criticidade e indicador visual (badge colorido) por cartão.

**Justificativa:** o desafio original da TechFlow Solutions menciona
explicitamente que o cliente busca "priorizar tarefas críticas" — requisito
que não estava coberto pela primeira versão do CRUD, restrita a título,
descrição e status. Sem um campo de prioridade, a equipe de logística não
teria como sinalizar, dentro do próprio sistema, quais tarefas exigem
atenção imediata — o que compromete diretamente um dos objetivos centrais
do projeto.

**Como a mudança foi gerenciada** (ver histórico completo no
`README.md` do repositório):

1. Um cartão específico para a mudança (*"Implementar mudança de escopo:
   prioridade das tarefas"*) foi criado no backlog (coluna **To Do**) do
   quadro Kanban antes mesmo de iniciar a implementação;
2. O cartão foi movido para **In Progress** no início do desenvolvimento;
3. A mudança foi implementada em um commit dedicado, cobrindo modelo,
   rotas, template, estilo visual e testes automatizados;
4. O pipeline de CI validou a mudança (lint + testes) antes de ser
   considerada concluída;
5. O cartão foi então movido para **Done**, e o `README.md` foi atualizado
   com a justificativa apresentada nesta seção.

Esse fluxo demonstra, em escala reduzida, como um projeto conduzido em
Kanban absorve mudanças de escopo sem interromper o trabalho em andamento:
a mudança entra como mais um item do backlog, é priorizada, implementada,
testada e validada como qualquer outra tarefa — sem necessidade de
renegociar um sprint inteiro, como aconteceria em um modelo baseado em
ciclos fixos.

## 6. Testes automatizados

Os testes foram implementados com **Pytest**, utilizando o cliente de
testes do Flask (`app.test_client()`) e um banco de dados SQLite em memória
isolado por teste (fixture `app`/`client` em `tests/conftest.py`).

A suíte cobre:

- **Autenticação**: cadastro de usuário, rejeição de campos obrigatórios
  vazios, rejeição de usuário duplicado, login com credenciais corretas e
  incorretas, logout, e bloqueio de acesso ao quadro sem autenticação;
- **CRUD de tarefas**: criação com validação de título obrigatório,
  atualização de status com rejeição de valores inválidos, exclusão, e
  isolamento de dados entre usuários diferentes (um usuário não pode
  alterar/excluir tarefas de outro — retorno HTTP 404);
- **Mudança de escopo (prioridade)**: criação de tarefa com prioridade
  válida, fallback para o valor padrão quando a prioridade informada é
  inválida, e atualização de prioridade com validação de entrada.

No total, a suíte conta com 17 testes automatizados, executados
automaticamente pelo pipeline de CI a cada `push`/`pull request` na branch
`main`, junto com uma verificação de qualidade de código via `flake8`. Essa
combinação garante que alterações futuras no código não quebrem
silenciosamente o comportamento esperado do sistema — um teste que falha
bloqueia visualmente o pipeline no GitHub Actions antes que o código
"quebrado" seja considerado pronto.

## 7. Prints comentados do GitHub

_(Inserir os três prints abaixo, cada um com uma legenda breve.)_

1. **Quadro Kanban** (aba *Projects* do repositório): mostrar as três
   colunas (To Do / In Progress / Done) com os cartões distribuídos
   conforme o andamento real do desenvolvimento.
2. **Commits relevantes** (aba *Commits* do repositório, ou `git log
   --oneline`): destacar a sequência de commits descritivos, incluindo o
   commit da mudança de escopo (`feat: adiciona campo de prioridade às
   tarefas (mudança de escopo)`).
3. **Workflow de CI funcionando** (aba *Actions* do repositório): mostrar
   uma execução com status "success", evidenciando os passos de lint
   (`flake8`) e testes (`pytest`) concluídos com sucesso.

## 8. Considerações finais

O desenvolvimento do TechFlow Task Manager permitiu aplicar, de forma
prática e integrada, conceitos centrais da disciplina: modelagem UML como
apoio à implementação, controle de versão com histórico de commits
significativo, organização do trabalho em um quadro Kanban, automação de
testes e integração contínua, e absorção controlada de uma mudança de
escopo — todos os pilares que sustentam a entrega confiável de software em
um contexto ágil real de mercado.

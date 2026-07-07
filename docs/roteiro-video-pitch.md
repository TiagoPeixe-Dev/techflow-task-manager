# Roteiro do Vídeo Pitch (até 4 minutos)

Grave a tela (aplicação rodando localmente + navegador no GitHub) com áudio
explicando cada etapa. Publique no YouTube (pode ser "não listado") ou Google
Drive com link público, e inclua o link na entrega.

Tempo total sugerido: **~3min40s**, com folga para os 4 minutos do limite.

---

### 1. Abertura (20s)

> "Olá, meu nome é Tiago. Este é o TechFlow Task Manager, um sistema de
> gerenciamento de tarefas desenvolvido para a TechFlow Solutions, empresa
> fictícia contratada por uma startup de logística, como parte do trabalho
> da disciplina de Engenharia de Software."

- Mostrar a tela inicial do repositório no GitHub (README renderizado).

### 2. Metodologia ágil e Kanban (40s)

> "O projeto foi conduzido com metodologia Kanban. Todo o planejamento foi
> feito na aba Projects do GitHub, com três colunas: To Do, In Progress e
> Done. Cada cartão representa uma unidade de trabalho que virou um ou mais
> commits no repositório."

- Abrir a aba **Projects** e mostrar o quadro com os cartões distribuídos.
- Passar o mouse/clicar em 1-2 cartões para mostrar a descrição.

### 3. Demonstração do sistema funcionando (60-70s)

> "Vamos ver o sistema rodando."

- Rodar `python run.py` no terminal (ou já deixar rodando antes de gravar).
- No navegador:
  1. Criar uma conta (`/register`);
  2. Fazer login;
  3. Criar 2-3 tarefas com prioridades diferentes;
  4. Mover uma tarefa de "A Fazer" para "Em Progresso" (mostrar o select de
     status);
  5. Mudar a prioridade de uma tarefa e mostrar o card reordenando/mudando
     de cor;
  6. Excluir uma tarefa.

### 4. Testes automatizados (30-40s)

> "Todo o comportamento do sistema é validado por testes automatizados
> escritos com Pytest."

- No terminal, rodar `pytest -v` e mostrar os testes passando (17 testes).
- Comentar rapidamente: "os testes cobrem cadastro, login, CRUD de tarefas,
  validação de entradas e o isolamento de dados entre usuários diferentes."

### 5. GitHub Actions / CI (30-40s)

> "A cada push no repositório, um pipeline de integração contínua roda
> automaticamente no GitHub Actions."

- Abrir a aba **Actions** do repositório.
- Mostrar uma execução com status de sucesso (✅), abrindo os passos de
  `flake8` (qualidade de código) e `pytest` (testes).

### 6. Mudança de escopo (30-40s)

> "Durante o desenvolvimento, simulamos uma mudança de escopo real: o
> cliente original pedia para priorizar tarefas críticas, mas a primeira
> versão do sistema não tinha esse campo. Adicionamos a prioridade das
> tarefas como uma nova funcionalidade."

- Mostrar o commit específico da mudança de escopo (`git log` ou aba
  Commits do GitHub).
- Mostrar a seção "Gestão de Mudanças" no `README.md`.
- Mostrar o cartão correspondente no Kanban (coluna Done).

### 7. Reflexão final (20-30s)

> "Esse projeto mostrou na prática como ferramentas como GitHub Projects,
> GitHub Actions e testes automatizados dão suporte real à Engenharia de
> Software: elas tornam o fluxo de trabalho visível, garantem que mudanças
> não quebrem o que já funciona, e permitem que a equipe absorva mudanças de
> escopo sem perder controle do projeto. São práticas que refletem
> diretamente o que se espera de um profissional de desenvolvimento no
> mercado de trabalho atual."

- Encerrar mostrando novamente a URL do repositório.

---

## Checklist antes de gravar

- [ ] Aplicação rodando localmente sem erros (`python run.py`)
- [ ] Banco de dados limpo (sem tarefas de teste antigas) — pode apagar
      `instance/techflow.db` antes de gravar
- [ ] Repositório público confirmado (URL acessível em aba anônima)
- [ ] Quadro Kanban com os cartões atualizados
- [ ] Última execução do GitHub Actions com status de sucesso
- [ ] `pytest -v` rodando sem falhas

# Diagrama de Casos de Uso — TechFlow Task Manager

Ator único: **Usuário** (colaborador da equipe que usa o sistema para
gerenciar suas próprias tarefas).

```mermaid
flowchart LR
    Usuario(["🧑 Usuário"])

    Usuario --> UC1[Cadastrar-se]
    Usuario --> UC2[Efetuar login]
    Usuario --> UC3[Efetuar logout]
    Usuario --> UC4[Criar tarefa]
    Usuario --> UC5[Listar tarefas no quadro Kanban]
    Usuario --> UC6[Atualizar status da tarefa]
    Usuario --> UC7[Atualizar prioridade da tarefa]
    Usuario --> UC8[Excluir tarefa]

    UC4 -.include.-> UC9[Validar título obrigatório]
    UC6 -.include.-> UC10[Validar status permitido]
    UC7 -.include.-> UC11[Validar prioridade permitida]
    UC5 -.include.-> UC2
    UC4 -.include.-> UC2
    UC6 -.include.-> UC2
    UC7 -.include.-> UC2
    UC8 -.include.-> UC2
```

## Descrição resumida dos casos de uso

| Caso de uso | Descrição |
|---|---|
| Cadastrar-se | Usuário cria uma conta informando usuário e senha; senha é armazenada com hash. |
| Efetuar login | Usuário autentica-se para acessar seu quadro de tarefas. |
| Efetuar logout | Usuário encerra a sessão autenticada. |
| Criar tarefa | Usuário adiciona uma nova tarefa (título obrigatório, descrição e prioridade opcionais). |
| Listar tarefas no quadro Kanban | Usuário visualiza suas tarefas organizadas nas colunas A Fazer / Em Progresso / Concluído, ordenadas por prioridade. |
| Atualizar status da tarefa | Usuário move a tarefa entre as colunas do quadro. |
| Atualizar prioridade da tarefa | Usuário reclassifica a tarefa entre baixa, média, alta ou crítica (funcionalidade adicionada na mudança de escopo). |
| Excluir tarefa | Usuário remove definitivamente uma tarefa. |

> Nota: para incluir este diagrama no documento da Parte Teórica (PDF/DOCX),
> renderize o bloco Mermaid acima em https://mermaid.live e exporte como
> imagem (PNG/SVG), ou tire um print da visualização do GitHub, que renderiza
> Mermaid nativamente em arquivos `.md`.

# minhas_skills_e_prompts

Este repositório reúne exemplos de prompts, skills e utilitários para apoiar a criação de experiências com IA generativa, com foco em simulação de provas e geração de prompts personalizados.

## O que há neste projeto

- `prompts/` — coleções de prompts prontos para uso.
  - `prompts/simulacao_concursos/` — prompt base para simulação de provas e um gerador CLI para personalizar esse prompt.
- `skills/` — exemplos de skills e instruções de sistema para uso com modelos de IA.
- `LICENSE` — licença MIT do projeto.

## Conteúdo principal

### 1. Simulador de provas
No diretório `prompts/simulacao_concursos/` você encontra:

- `simulador_prova_concurso.md` — prompt base com regras para atuar como banca examinadora.
- `app_cli/gerador_prompt.py` — script em Python que cria uma versão personalizada do prompt a partir de opções como banca, estilo da prova, consulta permitida e conteúdo programático.

### 2. Skills
No diretório `skills/` há um exemplo de skill em formato de instrução de sistema para uso em ambientes que suportam esse tipo de configuração.

## Como usar

### Gerar um prompt personalizado

1. Acesse a pasta do projeto.
2. Execute:

   ```bash
   python prompts/simulacao_concursos/app_cli/gerador_prompt.py
   ```

3. Informe os dados solicitados no menu interativo.
4. O arquivo gerado será salvo em `prompts_gerados/`.

## Estrutura do repositório

```text
.
├── LICENSE
├── README.md
├── prompts/
│   └── simulacao_concursos/
│       ├── README.md
│       ├── simulador_prova_concurso.md
│       └── app_cli/
│           └── gerador_prompt.py
└── skills/
    └── hgf_skill.md
```

## Licença

Este projeto está licenciado sob a licença MIT, conforme descrito em `LICENSE`.

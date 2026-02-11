import os

# Pasta onde os prompts serão salvos
PASTA_SAIDA = "prompts_gerados"

def criar_pasta():
    if not os.path.exists(PASTA_SAIDA):
        os.makedirs(PASTA_SAIDA)

def menu(titulo, opcoes):
    print(f"\n=== {titulo} ===")
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i}. {opcao}")
    escolha = int(input("Escolha uma opção: "))
    return opcoes[escolha - 1]

def entrada_multilinha(titulo):
    print(f"\n=== {titulo} ===")
    print("Cole o conteúdo abaixo. Quando terminar, digite: FIM (em uma nova linha)\n")
    linhas = []
    while True:
        linha = input()
        if linha.strip().upper() == "FIM":
            break
        linhas.append(linha)
    return "\n".join(linhas)

def gerar_prompt(config):
    return f"""
# PROMPT PERSONALIZADO - SIMULADOR DE PROVAS

Você deve se comportar EXCLUSIVAMENTE como um SIMULADOR DE PROVAS.

## CONFIGURAÇÕES EDITÁVEIS

- BANCA EXAMINADORA: {config['banca']}
- PERFIL DE QUESTÕES: {config['perfil']}
- ESTILO DA PROVA: {config['estilo']}
- CONSULTA: {config['consulta']}
- QUANTIDADE TOTAL DE QUESTÕES: {config['quantidade']}

---

## PERFIL DE BANCA

{config['perfil_descricao']}

---

## CONTEÚDO PROGRAMÁTICO

{config['conteudo']}

---

## DISTRIBUIÇÃO DE QUESTÕES E PESOS

{config['distribuicao']}

---

## CRITÉRIOS DE AVALIAÇÃO

{config['criterios']}

---

## REGRAS

1. Não cobrar conteúdo fora do edital.
2. Questões exclusivamente QME (4 alternativas, apenas 1 correta).
3. Não apresentar gabarito antes das respostas.
4. Aplicar rigor técnico conforme banca selecionada.
"""

def main():
    criar_pasta()

    bancas = ["FGV", "FCC", "CESPE/CEBRASPE", "ENADE"]
    perfis = {
        "FGV": "Enunciados longos, interpretativos, alternativas semanticamente próximas.",
        "FCC": "Questões literais, diretas e com termos absolutos.",
        "CESPE/CEBRASPE": "Alta precisão técnica, foco em exceções conceituais.",
        "ENADE": "Situações-problema contextualizadas e aplicação prática."
    }

    estilos = ["Literal", "Interpretativa", "Técnica", "Eliminatória", "Situação-problema"]
    consultas = ["Sem consulta", "Com consulta", "Consulta restrita ao edital"]

    banca_escolhida = menu("BANCA EXAMINADORA", bancas)
    perfil_escolhido = banca_escolhida
    estilo_escolhido = menu("ESTILO DA PROVA", estilos)
    consulta_escolhida = menu("CONSULTA", consultas)

    quantidade = input("\nQuantidade total de questões: ")

    conteudo = entrada_multilinha("CONTEÚDO PROGRAMÁTICO")
    distribuicao = entrada_multilinha("DISTRIBUIÇÃO DE QUESTÕES E PESOS")
    criterios = entrada_multilinha("CRITÉRIOS DE AVALIAÇÃO")

    config = {
        "banca": banca_escolhida,
        "perfil": perfil_escolhido,
        "perfil_descricao": perfis[perfil_escolhido],
        "estilo": estilo_escolhido,
        "consulta": consulta_escolhida,
        "quantidade": quantidade,
        "conteudo": conteudo,
        "distribuicao": distribuicao,
        "criterios": criterios
    }

    prompt_final = gerar_prompt(config)

    nome_arquivo = input("\nNome do arquivo (sem extensão): ")
    caminho = os.path.join(PASTA_SAIDA, f"{nome_arquivo}.md")

    with open(caminho, "w", encoding="utf-8") as f:
        f.write(prompt_final)

    print(f"\n✅ Prompt gerado com sucesso em: {caminho}")

if __name__ == "__main__":
    main()

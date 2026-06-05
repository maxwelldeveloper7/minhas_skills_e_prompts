---
name: hardware-svg-renderer
version: "2.0"
description: "Renderizador técnico de componentes de hardware em SVG 2D puro para jogos epistêmicos"
---

# Skill — Hardware SVG Renderer

## Identidade da Skill

Esta skill gera ilustrações hiper-realistas de componentes de hardware em SVG 2D puro,
prontas para uso como assets de front-end em jogos epistêmicos. Equilibra fidelidade
técnica com legibilidade pedagógica, produzindo código SVG autocontido, semanticamente
organizado e reutilizável.

---

## Configuração em YAML

```yaml
name: hardware-svg-renderer
version: "2.0"
description: >
  Especialista em renderização técnica de componentes de hardware em SVG 2D
  puro. Gera ilustrações hiper-realistas, semanticamente organizadas e prontas
  para uso em interfaces front-end de jogos epistêmicos — equilibrando
  fidelidade técnica com legibilidade pedagógica.

output:
  format: SVG puro (<svg>...</svg>)
  requisitos:
    - Autocontido e responsivo
    - Sem dependências externas (fontes, imagens, scripts)
    - Reutilizável como asset de UI

regras_de_ouro:
  - id: 1
    nome: Output SVG puro
    regra: >
      Entregar exclusivamente código SVG, sem Markdown externo ao bloco de
      código. Nenhum elemento deve depender de recursos externos.

  - id: 2
    nome: Estado avulso (pré-montagem)
    regra: >
      Por padrão, todo componente é renderizado isolado, como peça de estoque.
      Pinos, pads, esferas BGA e contatos devem ser limpos, intactos,
      simétricos e sem fusão física ou sinais de uso.

  - id: 3
    nome: Hiper-realismo por recursos nativos SVG
    regra: >
      Simular texturas físicas exclusivamente com recursos nativos SVG.
      Proibido usar imagens rasterizadas embutidas (base64).
    recursos_permitidos:
      - linearGradient
      - radialGradient
      - filter > feTurbulence
      - filter > feSpecularLighting
      - filter > feDropShadow
      - filter > feBlend

  - id: 4
    nome: Organização semântica obrigatória
    regra: >
      Agrupar cada camada funcional com <g id="..."> descritivo.
      IDs devem ser únicos e em kebab-case.
    exemplos_de_ids:
      - substrato
      - pins-row-a
      - label-serigrafia
      - anim-cooler

  - id: 5
    nome: Gate de complexidade
    regra: >
      Antes de renderizar qualquer componente com estimativa acima de 300
      elementos SVG, informar o custo estimado e aguardar confirmação
      do usuário.

  - id: 6
    nome: Modo Passo a Passo — herança obrigatória
    regra: >
      Quando ativo, cada fase deve entregar o SVG acumulado completo até
      aquele ponto. Nunca entregar fragmentos isolados. Cada fase exibe
      cabeçalho: [Fase X/Y — NomeDoBloco].

parametros:
  construcao:
    descricao: Modo de geração do SVG
    opcoes:
      - valor: Completo
        padrao: true
        descricao: SVG gerado integralmente em uma única entrega.
      - valor: Passo a Passo
        padrao: false
        descricao: >
          Construção faseada e acumulativa. Aguarda comando "próxima fase"
          para avançar.

  visualizacao_interna:
    descricao: Exposição de camadas internas do componente
    opcoes:
      - valor: Opaco
        padrao: true
        descricao: Renderização sólida e realista. Superfícies ocluem camadas internas.
      - valor: Raio-X
        padrao: false
        descricao: >
          Opacidade cirúrgica para expor die de silício, wire bonds e
          camadas de substrato.
      - valor: Explodido
        padrao: false
        descricao: >
          Separação vertical das camadas físicas com espaçamento uniforme
          e linhas-guia de eixo.

  acabamento_metalurgico:
    descricao: Paleta e textura dos contatos metálicos
    opcoes:
      - valor: ENIG
        nome_completo: Ouro Químico
        padrao: true
        cores:
          gradiente: "#C8A84B → #8B6914"
          estilo: dourado/âmbar fosco
      - valor: HASL
        nome_completo: Estanho/Prata
        padrao: false
        cores:
          gradiente: "#E8E8E8 → #A0A0A0"
          estilo: prateado brilhante com highlight especular
      - valor: Industrial Matte
        padrao: false
        cores:
          gradiente: "#2A2A2A → #1A1A1A"
          estilo: cinza escuro/preto com sombreamento difuso plano

  interatividade:
    descricao: Estados de interação para uso em front-end
    opcoes:
      - valor: Nenhuma
        padrao: true
        descricao: Asset estático puro.
      - valor: Hover
        padrao: false
        descricao: >
          Adiciona <style> interno com CSS :hover (highlight de borda,
          filter drop-shadow, cursor pointer).
      - valor: Selecao
        padrao: false
        descricao: >
          Estado .selected via classe CSS (borda colorida + label flutuante
          com nome do componente).
      - valor: Hover+Selecao
        padrao: false
        descricao: Ambos os estados combinados, prontos para bind via JavaScript externo.

  animacao:
    descricao: Movimento e dinâmica visual
    opcoes:
      - valor: Estatica
        padrao: true
        descricao: Sem movimento. Máxima compatibilidade.
      - valor: Ativada
        padrao: false
        descricao: Injeção de @keyframes CSS nativos do SVG.
        exemplos:
          cooler: rotate via animateTransform
          led: opacity pulsante
          fluxo_dados: stroke-dashoffset animado em trilhas de barramento

  marcacao_tecnica:
    descricao: Textos e indicadores serigrafados
    opcoes:
      - valor: Ativada
        padrao: true
        descricao: >
          Textos serigrafados (<text>), indicadores de orientação (▲ Pino 1,
          chanfro de encaixe), referências de modelo e fabricante.
      - valor: Desativada
        padrao: false
        descricao: Geometria limpa, sem texto. Ideal para assets de fundo ou decoração de UI.

  densidade_visual:
    descricao: Nível de detalhe e complexidade do asset
    opcoes:
      - valor: Esquematico
        padrao: false
        descricao: >
          Geometrias simplificadas. Prioriza legibilidade em tamanhos
          pequenos (ícones, miniaturas de UI).
      - valor: Pedagogico
        padrao: true
        descricao: >
          Equilíbrio entre fidelidade técnica e clareza. Detalha elementos
          funcionais relevantes sem poluição visual.
      - valor: Industrial
        padrao: false
        descricao: >
          Máxima fidelidade. Todos os pinos, vias, textos e texturas
          renderizados. Requer confirmação via gate de complexidade.

uso_em_jogos_epistemicos:
  viewbox: >
    Gerar componente com viewBox relativa ao seu bounding box próprio,
    sem margens fixas. Permite posicionamento livre por CSS/JS no front-end.
  ids_semanticos: >
    Garantir que grupos clicáveis tenham IDs semânticos (ex: slot-ram-1)
    para facilitar addEventListener externo.
  paleta_consistente: >
    Manter os mesmos valores de gradiente e filtros entre assets de uma
    mesma cena para coerência visual.

estrutura_de_resposta:
  ordem:
    - passo: 1
      nome: Confirmação de Parâmetros
      descricao: Bullet list dos parâmetros ativos (explícitos ou assumidos como padrão).
    - passo: 2
      nome: Análise Técnica
      descricao: >
        2–3 linhas descrevendo a lógica construtiva do componente, decisões
        de representação e simplificações pedagógicas aplicadas.
    - passo: 3
      nome: Gate de Complexidade
      descricao: Estimativa de elementos e aguardo de confirmação (se aplicável).
    - passo: 4
      nome: Bloco SVG
      descricao: Código dentro de bloco xml ou svg, limpo e funcional.
```

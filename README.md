# Análise de Carteira de Investimentos com Python

Projeto desenvolvido em Python com o objetivo de aplicar conceitos básicos de análise de investimentos e praticar programação aplicada ao mercado financeiro.

A análise utiliza dados históricos de PETR4 e VALE3 para construir uma carteira com pesos iguais entre os dois ativos. O desempenho da carteira é analisado por meio de métricas de retorno e risco e comparado com referências do mercado brasileiro.

## Summary (English)

Python analysis of a 50/50 PETR4/VALE3 portfolio over 2025 (January 2 to December 30), using Yahoo Finance prices and the CDI rate from the Central Bank of Brazil. The portfolio returned 19.5%, against 34.9% for the BOVA11 benchmark and 14.3% for the CDI, with a maximum drawdown of 15.2% (6.7% for BOVA11) and a Sharpe ratio of 0.30 (1.11 for BOVA11). Results are reported for a daily-rebalanced and a buy-and-hold version of the portfolio. This is a learning project, and its conclusions are limited to one year and two stocks.

## Principais Resultados

Período: de 2 de janeiro a 30 de dezembro de 2025 (250 pregões). Preços ajustados por proventos.

| Ativo | Retorno acumulado | Volatilidade anual | Sharpe Ratio | Drawdown máximo |
|---|---|---|---|---|
| PETR4 | -6,66% | 22,67% | -0,83 | -21,06% |
| VALE3 | 50,13% | 22,00% | 1,33 | -15,39% |
| BOVA11 (benchmark) | 34,93% | 15,56% | 1,11 | -6,73% |
| Carteira 50/50 (rebalanceada diariamente) | 19,54% | 17,43% | 0,30 | -15,21% |
| Carteira 50/50 (sem rebalancear) | 21,74% | 17,39% | 0,41 | -15,23% |
| CDI | 14,32% | n/a | n/a | n/a |

Como ler as colunas de diferença em relação ao BOVA11 no arquivo `tabela_resumo.csv`:

* `Dif. Acumulado vs BOVA11`: diferença entre os retornos acumulados. A carteira rebalanceada ficou 15,38 p.p. abaixo do BOVA11, e a carteira sem rebalancear, 13,19 p.p. abaixo.
* `Excesso vs BOVA11`: diferença entre os retornos médios anualizados (média diária multiplicada por 252, a mesma base usada no Sharpe). Por isso o valor da carteira rebalanceada (-12,08 p.p.) é diferente da diferença acumulada.

## Interpretação

* A carteira rendeu mais que o CDI (14,32%), mas ficou abaixo do BOVA11 com mais volatilidade (17,43% contra 15,56%) e queda máxima maior (15,21% contra 6,73%). Por isso o Sharpe ficou em 0,30, contra 1,11 do índice.
* O resultado vem de dois papéis com desempenhos opostos no período (PETR4 em -6,66% e VALE3 em +50,13%). A carteira reflete essas duas empresas, e não a diversificação de um índice.
* A correlação entre os retornos diários de PETR4 e VALE3 foi de 0,2176. Com ela, a volatilidade da carteira cai de cerca de 22% para 17,43%, o que confere com a fórmula abaixo. Mesmo assim, dois ativos não chegam à volatilidade do índice (15,56%).

$$\sigma_p = \sqrt{0{,}5^2\sigma_A^2 + 0{,}5^2\sigma_B^2 + 2 \cdot 0{,}5 \cdot 0{,}5\,\rho\,\sigma_A\sigma_B} \approx 17{,}43\%$$

* O rebalanceamento diário reduz o retorno acumulado em cerca de 2,2 p.p. (19,54% contra 21,74%), porque vende o ativo que sobe e compra o que cai todos os dias. Parte da defasagem para o BOVA11 vem dessa premissa, e não da escolha dos ativos.

## Limitações e Premissas

* A análise cobre um único ano e apenas dois ativos. O resultado depende do período e não permite concluir sobre a eficácia de uma estratégia.
* O retorno é medido a partir do fechamento de 2 de janeiro de 2025.
* A carteira "rebalanceada diariamente" reaplica 50/50 todos os dias, o que na prática teria custos. A versão sem rebalancear mantém os pesos iniciais.
* Não há custos de transação nem impostos.
* O Sharpe usa o retorno médio diário multiplicado por 252 e o CDI médio do período como taxa livre de risco.
* Os preços vêm do Yahoo Finance com ajuste por proventos. O histórico pode ser revisado, e os valores podem variar nas casas decimais ao reexecutar.

## Objetivos do Projeto

* Coletar dados históricos de ativos financeiros;
* Calcular retornos diários e acumulados;
* Calcular retorno médio anualizado;
* Calcular volatilidade anualizada;
* Calcular Sharpe Ratio;
* Analisar a correlação entre os ativos;
* Calcular drawdown e drawdown máximo;
* Comparar o desempenho dos ativos com o BOVA11;
* Construir uma carteira com 50% de PETR4 e 50% de VALE3;
* Comparar o desempenho acumulado da carteira com o CDI;
* Gerar uma tabela resumo das principais métricas;
* Criar visualizações do desempenho e do drawdown da carteira.

## Ativos Analisados

* PETR4.SA — Petrobras PN
* VALE3.SA — Vale ON
* BOVA11.SA — ETF utilizado como benchmark de mercado

A carteira analisada possui a seguinte composição:

* 50% PETR4
* 50% VALE3

O CDI é utilizado como referência para comparação do desempenho acumulado da carteira.

## Métricas Calculadas

O projeto calcula as seguintes métricas:

* Retorno médio;
* Retorno médio anualizado;
* Retorno acumulado;
* Volatilidade;
* Volatilidade anualizada;
* Sharpe Ratio;
* Correlação;
* Drawdown;
* Drawdown máximo;
* Excesso de retorno em relação ao BOVA11;
* Métricas da carteira 50/50 sem rebalanceamento (buy-and-hold);
* Diferença de retorno acumulado em relação ao BOVA11.

## Visualizações

### Carteira vs CDI

Compara a evolução do retorno acumulado da carteira 50/50 com o CDI durante o período analisado.

![Carteira vs CDI](carteira_vs_cdi.png)

### Drawdown da Carteira

Mostra as quedas da carteira em relação aos seus máximos históricos durante o período.

![Drawdown da Carteira](drawdown_carteira.png)

## Jupyter Notebook

Além do script principal `main.py`, o projeto possui uma versão em Jupyter Notebook:

`analise_carteira.ipynb`

O notebook apresenta a análise de forma passo a passo, separando:

* coleta dos dados;
* criação das funções;
* análise dos ativos;
* análise do BOVA11;
* construção da carteira 50/50;
* tabela resumo;
* comparação com o CDI;
* análise de drawdown.

Essa versão permite visualizar tabelas, gráficos e resultados diretamente ao longo da execução das células.

O notebook reproduz a análise da carteira rebalanceada diariamente. A versão sem rebalancear e a coluna de diferença acumulada estão no `main.py`.

## Tecnologias Utilizadas

* Python
* Pandas
* NumPy
* yfinance
* python-bcb
* Matplotlib
* Jupyter Notebook

## Fontes de Dados

Os preços históricos dos ativos são obtidos por meio da biblioteca `yfinance`.

Os dados do CDI são obtidos através do Sistema Gerenciador de Séries Temporais do Banco Central do Brasil utilizando a biblioteca `python-bcb`.

## Como Executar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Depois execute o script:

```bash
python main.py
```

Também é possível abrir:

```text
analise_carteira.ipynb
```

em um ambiente Jupyter para acompanhar a análise célula por célula.

## Arquivos Gerados

O programa gera automaticamente:

* `tabela_resumo.csv`
* `carteira_vs_cdi.png`
* `drawdown_carteira.png`

## Estrutura do Projeto

```text
brazilian-portfolio-analysis/
├── main.py
├── analise_carteira.ipynb
├── README.md
├── requirements.txt
├── .gitignore
├── tabela_resumo.csv
├── carteira_vs_cdi.png
└── drawdown_carteira.png
```

## Sobre o Projeto

Este projeto foi desenvolvido como parte do meu aprendizado inicial de Python aplicado a finanças.

O objetivo principal foi consolidar conceitos básicos de programação, manipulação de dados e análise de risco e retorno por meio de uma aplicação prática utilizando dados do mercado financeiro brasileiro.


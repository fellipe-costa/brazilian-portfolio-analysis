# Análise de Carteira de Investimentos com Python

Projeto desenvolvido em Python com o objetivo de aplicar conceitos básicos de análise de investimentos e praticar programação aplicada ao mercado financeiro.

A análise utiliza dados históricos de PETR4 e VALE3 para construir uma carteira com pesos iguais entre os dois ativos. O desempenho da carteira é analisado por meio de métricas de retorno e risco e comparado com referências do mercado brasileiro.

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
* Excesso de retorno em relação ao BOVA11.

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


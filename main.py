import pandas as pd
import numpy as np
import yfinance as yf
from bcb import sgs
import matplotlib.pyplot as plt

ativos = ["PETR4.SA", "VALE3.SA"]
ibov = ["BOVA11.SA"]
ativos_br = {"CDI": 4389}

dados = yf.download(
    ativos,
    start="2025-01-01",
    end="2025-12-31",
    auto_adjust=True,
    progress=False
)

benchmark = yf.download(
    ibov,
    start="2025-01-01",
    end="2025-12-31",
    auto_adjust=True,
    progress=False
)

dados_br = sgs.get(
    ativos_br,
    start="2025-01-01",
    end="2025-12-31"
)

precos = dados["Close"]
precos_benchmark = benchmark["Close"].squeeze()
taxa_livre_risco = dados_br["CDI"].mean() / 100

# Calcular Retornos
def calcular_retornos(dados_precos):
    retornos = dados_precos.pct_change().dropna()
    return retornos

# Calcular Volatilidade
def calcular_volatilidade(retornos):
    volatilidade = retornos.std()
    return volatilidade

# Calcular Volatilidade Anual
def anualizar_volatilidade(volatilidade, periodos=252):
    volatilidade_anual = volatilidade * np.sqrt(periodos)
    return volatilidade_anual

# Calcular Retorno Médio
def calcular_retorno_medio(retornos):
    retorno_medio = retornos.mean()
    return retorno_medio

# Calcular Retorno Médio Anual
def anualizar_retorno_medio(retorno_medio, periodos=252):
    retorno_medio_anual = retorno_medio * periodos
    return retorno_medio_anual

# Calcular Excesso de Retorno
def calcular_excesso_retorno(retorno_medio_anual, retorno_medio_anual_benchmark):
    excesso_retorno = retorno_medio_anual - retorno_medio_anual_benchmark
    return excesso_retorno

# Calcular Retorno Acumulado
def calcular_retorno_acumulado(retornos):
    retorno_acumulado = (1 + retornos).cumprod() - 1
    return retorno_acumulado

# Calcular Sharpe Ratio
def calcular_sharpe(retorno_medio_anual, taxa_livre_risco, volatilidade_anual):
    sharpe = (retorno_medio_anual - taxa_livre_risco) / volatilidade_anual
    return sharpe

# Calcular Correlação
def calcular_correlacao(retornos):
    if isinstance(retornos, pd.DataFrame):
        correlacao = retornos.corr()
        return correlacao

    return None

# Calcular Drawdown
def calcular_drawdown(retornos):
    acumulado = (1 + retornos).cumprod()
    pico_historico = acumulado.cummax()
    drawdown = acumulado / pico_historico - 1
    return drawdown

# Calcular Drawdown Máximo
def calcular_drawdown_max(drawdown):
    drawdown_max = drawdown.min()
    return drawdown_max

# Analisar Ativos
def analise_ativos(retornos, taxa_livre_risco, periodos=252):
    volatilidade = calcular_volatilidade(retornos)
    volatilidade_anual = anualizar_volatilidade(volatilidade, periodos)
    retorno_medio = calcular_retorno_medio(retornos)
    retorno_medio_anual = anualizar_retorno_medio(retorno_medio, periodos)
    retorno_acumulado = calcular_retorno_acumulado(retornos)
    sharpe = calcular_sharpe(retorno_medio_anual, taxa_livre_risco, volatilidade_anual)
    correlacao = calcular_correlacao(retornos)
    drawdown = calcular_drawdown(retornos)
    drawdown_max = calcular_drawdown_max(drawdown)

    resultado = {
        "volatilidade": volatilidade,
        "volatilidade_anual": volatilidade_anual,
        "retorno_medio": retorno_medio,
        "retorno_medio_anual": retorno_medio_anual,
        "retorno_acumulado": retorno_acumulado,
        "sharpe": sharpe,
        "correlacao": correlacao,
        "drawdown": drawdown,
        "drawdown_max": drawdown_max
    }

    return resultado

# Analisar Preços
def analisar_precos(dados_precos, taxa_livre_risco, periodos=252):
    retornos = calcular_retornos(dados_precos)
    resultado = analise_ativos(retornos, taxa_livre_risco, periodos)
    return retornos, resultado

# Analisar Benchmark
def analise_benchmark(precos_benchmark, taxa_livre_risco):
    retornos_benchmark = calcular_retornos(precos_benchmark)
    retorno_medio_benchmark = calcular_retorno_medio(retornos_benchmark)
    retorno_medio_anual_benchmark = anualizar_retorno_medio(retorno_medio_benchmark)
    retorno_acumulado_benchmark = calcular_retorno_acumulado(retornos_benchmark).iloc[-1]
    volatilidade_benchmark = calcular_volatilidade(retornos_benchmark)
    volatilidade_anual_benchmark = anualizar_volatilidade(volatilidade_benchmark)
    sharpe_benchmark = calcular_sharpe(retorno_medio_anual_benchmark, taxa_livre_risco, volatilidade_anual_benchmark)
    drawdown_benchmark = calcular_drawdown(retornos_benchmark)
    drawdown_benchmark_max = calcular_drawdown_max(drawdown_benchmark)

    resultado_benchmark = {
        "retornos_benchmark": retornos_benchmark,
        "retorno_medio_benchmark": retorno_medio_benchmark,
        "retorno_medio_anual_benchmark": retorno_medio_anual_benchmark,
        "retorno_acumulado_benchmark": retorno_acumulado_benchmark,
        "volatilidade_benchmark": volatilidade_benchmark,
        "volatilidade_anual_benchmark": volatilidade_anual_benchmark,
        "sharpe_benchmark": sharpe_benchmark,
        "drawdown_benchmark": drawdown_benchmark,
        "drawdown_benchmark_max": drawdown_benchmark_max
    }

    return resultado_benchmark

retornos, resultado = analisar_precos(precos, taxa_livre_risco)
resultado_benchmark = analise_benchmark(precos_benchmark, taxa_livre_risco)

# Calcular Excesso de Retorno
excesso_retorno = calcular_excesso_retorno(resultado["retorno_medio_anual"], resultado_benchmark["retorno_medio_anual_benchmark"])

# Mostrar Resultados dos Ativos
print("Retornos:")
print(retornos.head().map(lambda x: f"{x:.2%}"))

print("\nRetorno Médio:")
print(resultado["retorno_medio"])

print("\nRetorno Médio Anual:")
print(resultado["retorno_medio_anual"])

print("\nRetorno Acumulado:")
print(resultado["retorno_acumulado"])

print("\nVolatilidade:")
print(resultado["volatilidade"])

print("\nVolatilidade Anual:")
print(resultado["volatilidade_anual"])

print("\nSharpe Ratio:")
print(resultado["sharpe"])

print("\nCorrelação:")
print(resultado["correlacao"])

print("\nDrawdown:")
print(resultado["drawdown"])

print("\nDrawdown Máximo:")
print(resultado["drawdown_max"])

print("\nRetorno Médio Anual Benchmark:")
print(resultado_benchmark["retorno_medio_anual_benchmark"])

print("\nRetorno Acumulado do Benchmark:")
print(resultado_benchmark["retorno_acumulado_benchmark"])

print("\nVolatilidade do Benchmark:")
print(resultado_benchmark["volatilidade_benchmark"])

print("\nVolatilidade Anual do Benchmark:")
print(resultado_benchmark["volatilidade_anual_benchmark"])

print("\nSharpe Ratio do Benchmark:")
print(resultado_benchmark["sharpe_benchmark"])

print("\nDrawdown Máximo do Benchmark:")
print(resultado_benchmark["drawdown_benchmark_max"])

print("\nExcesso de Retorno:")
print(excesso_retorno)

# Criar Carteira 50% PETR4 + 50% VALE3
pesos = np.array([0.5, 0.5])
retornos_carteira = retornos.dot(pesos)
resultado_carteira = analise_ativos(retornos_carteira, taxa_livre_risco)
retorno_acumulado_carteira_final = resultado_carteira["retorno_acumulado"].iloc[-1]

# Criar Tabela Resumo
retorno_acumulado_final = resultado["retorno_acumulado"].iloc[-1]

tabela_resumo = pd.DataFrame({
    "Retorno Anual": resultado["retorno_medio_anual"],
    "Retorno Acumulado": retorno_acumulado_final,
    "Volatilidade Anual": resultado["volatilidade_anual"],
    "Sharpe Ratio": resultado["sharpe"],
    "Drawdown Máximo": resultado["drawdown_max"],
    "Excesso vs BOVA11": excesso_retorno
})

# Adicionar BOVA11
tabela_resumo.loc["BOVA11.SA"] = [
    resultado_benchmark["retorno_medio_anual_benchmark"],
    resultado_benchmark["retorno_acumulado_benchmark"],
    resultado_benchmark["volatilidade_anual_benchmark"],
    resultado_benchmark["sharpe_benchmark"],
    resultado_benchmark["drawdown_benchmark_max"],
    0
]

# Adicionar Carteira 50/50
tabela_resumo.loc["CARTEIRA 50/50"] = [
    resultado_carteira["retorno_medio_anual"],
    retorno_acumulado_carteira_final,
    resultado_carteira["volatilidade_anual"],
    resultado_carteira["sharpe"],
    resultado_carteira["drawdown_max"],
    resultado_carteira["retorno_medio_anual"] - resultado_benchmark["retorno_medio_anual_benchmark"]
]

# Formatar Tabela
tabela_formatada = tabela_resumo.copy()

colunas_percentuais = [
    "Retorno Anual",
    "Retorno Acumulado",
    "Volatilidade Anual",
    "Drawdown Máximo",
    "Excesso vs BOVA11"
]

for coluna in colunas_percentuais:
    tabela_formatada[coluna] = tabela_formatada[coluna].map(lambda x: f"{x:.2%}")

tabela_formatada["Sharpe Ratio"] = tabela_formatada["Sharpe Ratio"].map(lambda x: f"{x:.2f}")

print("\nTabela Resumo:")
print(tabela_formatada)

# Salvar Tabela Resumo
tabela_resumo.to_csv("tabela_resumo.csv")

# Retorno Acumulado da Carteira
retorno_acumulado_carteira = calcular_retorno_acumulado(retornos_carteira)

# Retorno Acumulado do CDI
taxa_cdi_anual = dados_br["CDI"] / 100
taxa_cdi_diaria = (1 + taxa_cdi_anual) ** (1 / 252) - 1
retorno_acumulado_cdi = (1 + taxa_cdi_diaria).cumprod() - 1

# Gráfico: Carteira vs CDI
plt.figure(figsize=(10, 6))

plt.plot(
    retorno_acumulado_carteira.index,
    retorno_acumulado_carteira,
    label="Carteira 50/50"
)

plt.plot(
    retorno_acumulado_cdi.index,
    retorno_acumulado_cdi,
    label="CDI"
)

plt.title("Desempenho Acumulado: Carteira vs CDI - 2025")
plt.xlabel("Data")
plt.ylabel("Retorno Acumulado")
plt.legend()
plt.grid()

# Salvar Gráfico
plt.savefig("carteira_vs_cdi.png", dpi=300, bbox_inches="tight")

plt.show()

# Drawdown da Carteira
drawdown_carteira = calcular_drawdown(retornos_carteira)

# Gráfico: Drawdown da Carteira
plt.figure(figsize=(10, 6))

plt.plot(
    drawdown_carteira.index,
    drawdown_carteira,
    label="Drawdown da Carteira"
)

plt.title("Drawdown da Carteira - 2025")
plt.xlabel("Data")
plt.ylabel("Drawdown")
plt.legend()
plt.grid()

# Salvar Gráfico
plt.savefig("drawdown_carteira.png", dpi=300, bbox_inches="tight")

plt.show()

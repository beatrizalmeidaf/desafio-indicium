# Análise - Nome do Local e Preço

import pandas as pd
import matplotlib.pyplot as plt

def analisar_precos_por_bairro(data, bairros_originais, bairros_group_originais):
    """
    Analisa e visualiza os preços médios por bairro em um gráfico de barras horizontais.
    
    Parâmetros:
    - data: DataFrame contendo os dados de preços
    - bairros_originais: Lista de bairros originais
    - bairros_group_originais: Lista de grupos de bairros originais
    
    Etapas:
    1. Agrupa os dados por bairro e grupo de bairro original
    2. Calcula a média de preços e contagem de imóveis
    3. Ordena os resultados por preço médio em ordem decrescente
    4. Gera um gráfico de barras horizontais com os 10 bairros de maior preço médio
    5. Exibe os valores de preço médio em cada barra
    6. Imprime a tabela dos 10 bairros com maiores preços médios
    
    Retorna um DataFrame com as estatísticas de preço por bairro.
    """

    # DataFrame que combina grupo e bairro original em relação ao preço
    media_price_detalhado = data.groupby(['bairro_group_original', 'bairro_original'])['price'].agg(['mean', 'count']).reset_index()
    
    # ordena por preço médio em ordem decrescente
    media_price_detalhado = media_price_detalhado.sort_values('mean', ascending=False)
    
    # gráfico com top 10 maiores
    plt.figure(figsize=(18, 6))
    
    # gráfico de barras horizontais para melhor legibilidade
    top_10 = media_price_detalhado.head(10)
    
    plt.barh(top_10['bairro_original'] + ' (' + top_10['bairro_group_original'] + ')', 
             top_10['mean'], 
             color='#1C356A')
    
    plt.title("Top 10 Bairros por Preço Médio", fontsize=15)
    plt.xlabel("Preço Médio", fontsize=12)
    plt.ylabel("Bairro (Grupo)", fontsize=12)
    
    # valores maiores no começo do gráfico
    plt.gca().invert_yaxis()

    # adiciona os valores de preço médio nas barras
    for i, v in enumerate(top_10['mean']):
        plt.text(v, i, f' ${v:,.2f}', va='center', fontweight='bold')
    
    plt.tight_layout()
    plt.show()
    
    print("Top 10 Bairros por Preço Médio:")
    print(media_price_detalhado.head(10).to_string(index=False))
    
    return media_price_detalhado
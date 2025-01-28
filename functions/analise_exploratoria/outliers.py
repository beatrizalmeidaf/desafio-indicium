# Tratamento de Outliers

import matplotlib.pyplot as plt
import seaborn as sns

""" Substituição de Outlier pelos Limites
Útil para preservar os dados, mas reduzir o impacto dos outliers. Esses limites são definidos pelo IQR. 
Nesses casos, também poderia remover os outliers, porém geraria mais valores nulos, então para simplificar irei somente substituir pelos limites"""

def price_outliers(data, column):
    """
    Gera dois boxplots lado a lado para análise de outliers na coluna de preços:
    um antes e outro após o ajuste baseado no IQR.

    Parâmetros:
    - data: DataFrame contendo os dados.
    - column: Nome da coluna para análise de preços.
    """

    # cálculo do IQR
    Q1 = data[column].quantile(0.25)  # primeiro quartil
    Q3 = data[column].quantile(0.75)  # terceiro quartil
    IQR = Q3 - Q1                     # intervalo interquartil

    # definição dos limites
    limite_inferior = data[column].min()
    limite_superior = Q3 + 1.5 * IQR

    print(f"Limite inferior: {limite_inferior}")
    print(f"Limite superior: {limite_superior}")

    # cópia para preservar os dados originais para comparação de gráficos
    data_original = data[column].copy()

    # ajuste dos valores com a substituição
    data_ajustada = data[column].clip(lower=limite_inferior, upper=limite_superior)

    # boxplots
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # boxplot antes do ajuste (horizontal)
    sns.boxplot(data=data_original, orient='h', color='#FF6F61', fliersize=5, linewidth=2, whis=1.5, ax=axes[0])
    axes[0].set_title('Antes do Ajuste de Outliers', fontsize=14, fontweight='bold')
    axes[0].set_ylabel('Preço', fontsize=12)
    axes[0].grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

    # boxplot depois do ajuste (horizontal)
    sns.boxplot(data=data_ajustada, orient='h', color='#189FDB', fliersize=5, linewidth=2, whis=1.5, ax=axes[1])
    axes[1].set_title('Depois do Ajuste de Outliers', fontsize=14, fontweight='bold')
    axes[1].set_ylabel('Preço', fontsize=12)
    axes[1].grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

    plt.suptitle('Análise de Outliers - Preços', fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.show()

def noite_outliers(data, column='minimo_noites'):
    """
    Gera dois boxplots lado a lado para análise de outliers em uma coluna de mínimo de noites:
    um antes e outro após o ajuste baseado no IQR.

    Parâmetros:
    - data: DataFrame contendo os dados.
    - column: Nome da coluna para análise.
    """

    # cálculo do IQR
    Q1 = data[column].quantile(0.25)  # primeiro quartil
    Q3 = data[column].quantile(0.75)  # terceiro quartil
    IQR = Q3 - Q1                     # intervalo interquartil

    # definição dos limites
    limite_inferior = data[column].min()
    limite_superior = Q3 + 1.5 * IQR

    print(f"Limite inferior: {limite_inferior}")
    print(f"Limite superior: {limite_superior}")

    # cópia para preservar os dados originais para comparação de gráficos
    data_original = data[column].copy()

    # ajuste dos valores com a substituição
    data_ajustada = data[column].clip(lower=limite_inferior, upper=limite_superior)

    # boxplots
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # boxplot antes do ajuste (horizontal)
    sns.boxplot(x=data_original, orient='h', color='#FF6F61', fliersize=5, linewidth=2, whis=1.5, ax=axes[0])
    axes[0].set_title('Antes do Ajuste de Outliers', fontsize=14, fontweight='bold')
    axes[0].set_ylabel('Mínimo de Noites', fontsize=12)
    axes[0].grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

    # boxplot depois do ajuste (horizontal)
    sns.boxplot(x=data_ajustada, orient='h', color='#189FDB', fliersize=5, linewidth=2, whis=1.5, ax=axes[1])
    axes[1].set_title('Depois do Ajuste de Outliers', fontsize=14, fontweight='bold')
    axes[1].set_ylabel('Mínimo de Noites', fontsize=12)
    axes[1].grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

    plt.suptitle('Análise de Outliers - Mínimo de Noites', fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.show()

def reviews_outliers(data, column='numero_de_reviews'):
    """
    Análise de outliers para o número de reviews.
    
    Parâmetros:
    - data: DataFrame com os dados
    - column: Coluna para análise de outliers
    
    Gera boxplots comparativos antes e após ajuste de outliers.
    """

    # cálculo dos quartis e intervalo interquartil
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1

    # definição dos limites de outliers
    limite_inferior = data[column].min()
    limite_superior = Q3 + 1.5 * IQR

    print(f"Limite inferior: {limite_inferior}")
    print(f"Limite superior: {limite_superior}")

    # cópia para comparação
    data_original = data[column].copy()

    # ajuste dos outliers
    data_ajustada = data[column].clip(lower=limite_inferior, upper=limite_superior)

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # boxplot dos dados originais
    sns.boxplot(x=data_original, orient='h', color='#FF6F61', fliersize=5, linewidth=2, whis=1.5, ax=axes[0])
    axes[0].set_title('Antes do Ajuste de Outliers', fontsize=14, fontweight='bold')
    axes[0].set_ylabel('Número de Reviews', fontsize=12)
    axes[0].grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

    # boxplot dos dados ajustados
    sns.boxplot(x=data_ajustada, orient='h', color='#189FDB', fliersize=5, linewidth=2, whis=1.5, ax=axes[1])
    axes[1].set_title('Depois do Ajuste de Outliers', fontsize=14, fontweight='bold')
    axes[1].set_ylabel('Número de Reviews', fontsize=12)
    axes[1].grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

    plt.suptitle('Análise de Outliers - Número de Reviews', fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.show()

def reviews_por_mes_outliers(data, column='reviews_por_mes'):
    """
    Análise de outliers para reviews por mês.
    
    Parâmetros:
    - data: DataFrame com os dados
    - column: Coluna para análise de outliers
    
    Gera boxplots comparativos antes e após ajuste de outliers.
    """

    # cálculo dos quartis e intervalo interquartil
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1

    # definição dos limites
    limite_inferior = data[column].min()
    limite_superior = Q3 + 1.5 * IQR

    print(f"Limite inferior: {limite_inferior}")
    print(f"Limite superior: {limite_superior}")

    data_original = data[column].copy()

    # substituição de outliers
    data_ajustada = data[column].clip(lower=limite_inferior, upper=limite_superior)

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    sns.boxplot(x=data_original, orient='h', color='#FF6F61', fliersize=5, linewidth=2, whis=1.5, ax=axes[0])
    axes[0].set_title('Antes do Ajuste de Outliers', fontsize=14, fontweight='bold')
    axes[0].set_ylabel('Reviews por Mês', fontsize=12)
    axes[0].grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

    sns.boxplot(x=data_ajustada, orient='h', color='#189FDB', fliersize=5, linewidth=2, whis=1.5, ax=axes[1])
    axes[1].set_title('Depois do Ajuste de Outliers', fontsize=14, fontweight='bold')
    axes[1].set_ylabel('Reviews por Mês', fontsize=12)
    axes[1].grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

    plt.suptitle('Análise de Outliers - Reviews por Mês', fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.show()

def host_listings_outliers(data, column='calculado_host_listings_count'):
    """
    Análise de outliers para número de listings do host.
    
    Parâmetros:
    - data: DataFrame com os dados
    - column: Coluna para análise de outliers
    
    Gera boxplots comparativos antes e após ajuste de outliers.
    """

    # cálculo dos quartis e intervalo interquartil
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1

    # definição de limites
    limite_inferior = data[column].min()
    limite_superior = Q3 + 1.5 * IQR

    print(f"Limite inferior: {limite_inferior}")
    print(f"Limite superior: {limite_superior}")

    data_original = data[column].copy()

    # substituição dos outliers pelos limites
    data_ajustada = data[column].clip(lower=limite_inferior, upper=limite_superior)

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    sns.boxplot(x=data_original, orient='h', color='#FF6F61', fliersize=5, linewidth=2, whis=1.5, ax=axes[0])
    axes[0].set_title('Antes do Ajuste de Outliers', fontsize=14, fontweight='bold')
    axes[0].set_ylabel('Listings do Host', fontsize=12)
    axes[0].grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

    sns.boxplot(x=data_ajustada, orient='h', color='#189FDB', fliersize=5, linewidth=2, whis=1.5, ax=axes[1])
    axes[1].set_title('Depois do Ajuste de Outliers', fontsize=14, fontweight='bold')
    axes[1].set_ylabel('Listings do Host', fontsize=12)
    axes[1].grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

    plt.suptitle('Análise de Outliers - Listings do Host', fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.show()
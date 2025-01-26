# Análise e Tratamento de Valores Ausentes

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

def plot_top_names(data, column, top_n=20):
    """
    Gera um gráfico de barras com os nomes mais frequentes.

    Parâmetros:
    - data: DataFrame contendo os dados.
    - column: Nome da coluna para análise de frequência.
    - top_n: Número de valores mais frequentes a serem exibidos.
    """

    # conta as frequências dos valores na coluna
    name_counts = data[column].value_counts()
    top_names = name_counts.head(top_n)
    
    # gráfico
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=top_names.values,
        y=top_names.index,
        hue=top_names.index,
        legend=False,
        palette=sns.light_palette("#1C356A", reverse=True, n_colors=len(top_names))
    )
    
    plt.title(f'Frequência dos {top_n} Nomes Mais Comuns', fontsize=16, weight='bold')
    plt.xlabel('Frequência', fontsize=14)
    plt.ylabel(column, fontsize=14)
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    plt.show()


def plot_top_host_names(data, column, top_n=20):
    """
    Gera um gráfico de barras com os host names mais frequentes.

    Parâmetros:
    - data: DataFrame contendo os dados.
    - column: Nome da coluna para análise de frequência.
    - top_n: Número de valores mais frequentes a serem exibidos.
    """
    
    # conta as frequências dos valores na coluna
    host_name_counts = data[column].value_counts()
    top_host_names = host_name_counts.head(top_n)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=top_host_names.values,
        y=top_host_names.index,
        hue=top_host_names.index,
        legend=False,
        palette=sns.light_palette("#1C356A", reverse=True, n_colors=len(top_host_names))
    )
    
    plt.title(f'Frequência dos {top_n} Host Names Mais Comuns', fontsize=16, weight='bold')
    plt.xlabel('Frequência', fontsize=14)
    plt.ylabel(column, fontsize=14)
    plt.grid(axis='x', linestyle='--', alpha=0.6)
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    plt.show()


def plot_ultimo_review(data, column):
    """
    Gera um gráfico de série temporal com a distribuição das últimas revisões.

    Parâmetros:
    - data: DataFrame contendo os dados.
    - column: Nome da coluna contendo as datas para análise temporal.
    """
    
    # ordena os dados por data
    sorted_data = data.sort_values(by=column)

    plt.figure(figsize=(12, 6))
    plt.plot(
        sorted_data[column],
        range(len(sorted_data)),
        marker='o',
        linestyle='-',
        color='#1C356A',
        label='Revisões'
    )

    plt.title('Distribuição Temporal das Últimas Revisões', fontsize=16, fontweight='bold', pad=15)
    plt.xlabel('Data da Última Revisão', fontsize=12, labelpad=10)
    plt.ylabel('Índice', fontsize=12, labelpad=10)

    # formatação do eixo X
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))  # formato: Mês Ano
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6))  # intervalo de 6 meses
    plt.xticks(rotation=45, fontsize=10)

    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
    plt.legend(fontsize=12, loc='upper left')
    plt.tight_layout()

    plt.show()


def plot_reviews_distribuicao(data, column, bins=30):
    """
    Gera um histograma e um gráfico de densidade para os valores de uma coluna do dataset.

    Parâmetros:
    - data: DataFrame contendo os dados.
    - column: Nome da coluna para análise de distribuição.
    - bins: Número de bins no histograma.
    """

    # armazena os valores da coluna
    reviews_values = data[column].values

    fig, ax = plt.subplots(1, 2, figsize=(18, 6))

    # gráfico de histograma
    sns.histplot(reviews_values, bins=bins, kde=False, color='#1C356A', edgecolor='black', ax=ax[0])
    ax[0].set_title('Histograma dos Reviews por Mês', fontsize=14, fontweight='bold')
    ax[0].set_xlabel('Reviews por Mês', fontsize=12)
    ax[0].set_ylabel('Frequência', fontsize=12)
    ax[0].grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)

    # gráfico de densidade
    sns.kdeplot(reviews_values, color='r', fill=True, alpha=0.6, ax=ax[1])
    ax[1].set_title('Densidade dos Reviews por Mês', fontsize=14, fontweight='bold')
    ax[1].set_xlabel('Reviews por Mês', fontsize=12)
    ax[1].set_ylabel('Densidade', fontsize=12)
    ax[1].grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)


    plt.tight_layout()
    plt.show()
# Verifica se o número mínimo de noites e a disponibilidade ao longo do ano interferem no preço

import matplotlib.pyplot as plt
import seaborn as sns

def scatter_plot(data):
    """
    Plota gráficos de dispersão para analisar a relação entre 'minimo_noites',
    'disponibilidade_365' e 'price'.

    Parâmetros:
    data (DataFrame): DataFrame contendo as colunas 'minimo_noites', 
                      'disponibilidade_365' e 'price'.

    Retorno:
    None
    """

    plt.figure(figsize=(16, 6))

    # scatter plot 1: minimo_noites vs price
    plt.subplot(1, 2, 1)
    sns.scatterplot(
        x=data['minimo_noites'], 
        y=data['price'], 
        alpha=0.7, 
        color="#189FDB"
    )
    plt.title('Relação entre Mínimo de Noites e Preço')
    plt.xlabel('Mínimo de Noites')
    plt.ylabel('Preço')

    # scatter plot 2: disponibilidade_365 vs price
    plt.subplot(1, 2, 2)
    sns.scatterplot(
        x=data['disponibilidade_365'], 
        y=data['price'], 
        alpha=0.7, 
        color="#1C356A"
    )
    plt.title('Relação entre Disponibilidade 365 e Preço')
    plt.xlabel('Disponibilidade (em dias)')
    plt.ylabel('Preço')

    plt.tight_layout()
    plt.show()
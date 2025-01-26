# Análise Gráfica e Resumo dos Dados

import folium

def criar_mapa_apartamentos(data):
    """
    Cria um mapa interativo de apartamentos com marcadores coloridos baseados em preço e número de reviews.
    
    Parâmetros:
    - data: DataFrame contendo informações de apartamentos, incluindo latitude, longitude, preço e número de reviews
    
    Etapas:
    1. Centraliza o mapa na média das coordenadas do conjunto de dados
    2. Adiciona marcadores de círculo com cores variadas:
       - Verde: Preço < $50 e mais de 100 reviews
       - Amarelo: Preço < $100 e mais de 50 reviews
       - Laranja: Preço < $200
       - Vermelho: Preço >= $200
    3. Cada marcador inclui popup com informações do apartamento (bairro, preço, número de reviews)
    
    Retorna um objeto de mapa interativo criado com Folium.
    """
    
    # criação do mapa centralizado pela média das coordenadas
    mapa = folium.Map(
        location=[data['latitude'].mean(), data['longitude'].mean()],
        zoom_start=12
    )
    
    # marcadores de círculo coloridos
    for _, row in data.iterrows():
        # definição de cor baseada no preço e número de reviews
        if row['price'] < 50 and row['numero_de_reviews'] > 100:
            cor = 'green'
        elif row['price'] < 100 and row['numero_de_reviews'] > 50:
            cor = 'yellow'
        elif row['price'] < 200:
            cor = 'orange'
        else:
            cor = 'red'
        
        # adição do marcador ao mapa
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=8,
            color=cor,
            fill=True,
            fill_color=cor,
            fill_opacity=0.6,
            popup=f"Bairro: {row['bairro']}, Preço: ${row['price']}, Reviews: {row['numero_de_reviews']}" # quando clicar em cima do circulo verá essas informações
        ).add_to(mapa)
    
    return mapa

def analisar_bairros(data):
    """
    Analisa características de bairros para potencial investimento em aluguel.
    
    Parâmetros:
    - data: DataFrame com informações de apartamentos
    
    Etapas:
    1. Classifica imóveis por cores baseadas em preço e número de reviews:
       - Verde: Preço < $50 e +100 reviews (Ótimo para aluguel)
       - Amarelo: Preço < $100 e +50 reviews (Bom para aluguel)
       - Laranja: Preço < $200 (Intermediário)
       - Vermelho: Preço >= $200 (Menos recomendado)
    
    2. Calcula distribuição percentual de cores por bairro
    3. Ordena bairros pelo percentual de imóveis verdes e amarelos
    4. Gera relatório detalhado de análise de investimento
    5. Salva relatório em arquivo txt
    
    Retorna:
    - DataFrame de contagem de imóveis por cor e bairro
    - DataFrame de percentuais de imóveis por cor e bairro
    """

    def definir_cor(row):
        if row['price'] < 50 and row['numero_de_reviews'] > 100:
            return 'green'
        elif row['price'] < 100 and row['numero_de_reviews'] > 50:
            return 'yellow'
        elif row['price'] < 200:
            return 'orange'
        else:
            return 'red'
    
    data['cor'] = data.apply(definir_cor, axis=1)
    
    cores = ['green', 'yellow', 'orange', 'red']
    
    resumo_bairros = data.groupby('bairro_original')['cor'].value_counts().unstack(fill_value=0)
    
    # adiciona colunas de cores ausentes se elas não existirem
    for cor in cores:
        if cor not in resumo_bairros.columns:
            resumo_bairros[cor] = 0
    
    resumo_percentual = resumo_bairros.div(resumo_bairros.sum(axis=1), axis=0) * 100
    
    # ordenação por soma de percentuais de green e yellow (bons investimentos)
    bairros_ordenados = resumo_percentual.assign(
        total_verde_amarelo=resumo_percentual['green'] + resumo_percentual['yellow']
    ).sort_values('total_verde_amarelo', ascending=False)
    
    # resumo na saída do notebook
    output_lines = []
    output_lines.append("Análise de Bairros para Aluguel (Ordenado por Avaliação de Potencial Investimento):\n")
    
    for bairro in bairros_ordenados.index:
        linhas_bairro = [f"Bairro: {bairro}", f"Total de imóveis: {resumo_bairros.loc[bairro].sum()}"]
        for cor in cores:
            percentual = resumo_percentual.loc[bairro, cor]
            if percentual > 0:
                if cor == 'green':
                    linhas_bairro.append(f"Green (Ótimo para aluguel): {percentual:.2f}%")
                elif cor == 'yellow':
                    linhas_bairro.append(f"Yellow (Bom para aluguel): {percentual:.2f}%")
                elif cor == 'orange':
                    linhas_bairro.append(f"Orange (Intermediário): {percentual:.2f}%")
                elif cor == 'red':
                    linhas_bairro.append(f"Red (Menos recomendado): {percentual:.2f}%")
        linhas_bairro.append("\n")
        output_lines.append("\n".join(linhas_bairro))
    
    # imprime as primeiras análises
    print("\n".join(output_lines[:5]))  

    # salva toda a análise em um txt
    with open("data/analise_investimento_imoveis.txt", "w") as f:
        f.write("\n".join(output_lines))

    print("Arquivo txt salvo com sucesso na pasta 'data'")
    
    return resumo_bairros, resumo_percentual
import category_encoders as ce
import pandas as pd

def target_encoding(data, columns, target='price'):
    """
    Realiza target encoding nas colunas especificadas e salva a associação
    entre os valores originais e os valores codificados para serem usados posteriormente nos testes do modelo.
    
    Args:
        data (pd.DataFrame): Dataframe de entrada
        columns (list): Colunas para encodar
        target (str): Variável alvo para encoding
    
    Returns:
        pd.DataFrame: Dataframe com colunas encodadas por target
        dict: Dicionário contendo as associações entre valores originais e encodados
    """
    mappings = {}
    
    for col in columns:
        # cria um codificador de target para a coluna
        encoder = ce.TargetEncoder()
        
        # aplica o target encoding e salva o mapeamento dos valores
        encoded_values = encoder.fit_transform(data[col], data[target])
        mappings[col] = dict(zip(data[col], encoded_values[col]))
        
        # substitui a coluna original pelos valores encodados
        data[col] = encoded_values[col]
    
    return data, mappings

def one_hot_encoding(data, columns):
    """
    Realiza one-hot encoding nas colunas de menores dimensionalidade e converte 
    as colunas criadas para binário (0 e 1).
    
    Args:
        data (pd.DataFrame): Dataframe de entrada.
        columns (list): Colunas para one-hot encoding.
    
    Returns:
        pd.DataFrame: Dataframe com colunas one-hot encodadas.
    """
    # mantém o índice das colunas antes do encoding
    colunas_originais = set(data.columns)
    
    # aplica get_dummies para criar encodings one-hot
    data = pd.get_dummies(data, columns=columns)
    
    # identifica as novas colunas geradas pelo one-hot encoding
    novas_colunas = list(set(data.columns) - colunas_originais)
    
    # converte as novas colunas para int (binário) pois antes estava saindo em True ou False
    data[novas_colunas] = data[novas_colunas].astype(int)
    
    return data

def transformar_data(data, coluna):
    """
    Transforma uma coluna datetime em colunas separadas de ano, mês e dia.

    Parâmetros:
    - df (pd.DataFrame): DataFrame original.
    - coluna (str): Nome da coluna com dados no formato datetime.

    Retorna:
    - pd.DataFrame: DataFrame com as colunas 'ano', 'mes' e 'dia' adicionadas.
    """
    # garante que a coluna tá no formato datetime
    data[coluna] = pd.to_datetime(data[coluna], errors='coerce')
    
    # cria as colunas de ano, mês e dia
    data['ano'] = data[coluna].dt.year
    data['mes'] = data[coluna].dt.month
    data['dia'] = data[coluna].dt.day
    
    # remove a coluna original (opcional)
    data = data.drop(columns=[coluna])
    
    return data

def transformar_colunas_categoricas_dataset_teste(dataset_teste, mappings):
    """
    Aplica o mapeamento de target encoding no DataFrame de teste.
    
    Args:
        dataset_teste (pd.DataFrame): DataFrame de teste.
        mappings (dict): Dicionário com os mapeamentos do treinamento.
    
    Returns:
        pd.DataFrame: DataFrame de teste com as colunas encodadas.
    """

    for col, mapping in mappings.items():
        if col in dataset_teste.columns:
            # substitui os valores originais pelos valores encodados
            dataset_teste[col] = dataset_teste[col].map(mapping)
            
            # lida com valores não encontrados no mapeamento
            dataset_teste[col].fillna(-1, inplace=True)  
    
    return dataset_teste
# Desafio Técnico - Cientista de Dados 🚀  
**Programa Lighthouse - Indicium**

<div align="center">
  <img src="https://github.com/user-attachments/assets/c8b636a6-9475-4ddb-8bd9-f9f80da3c424" alt="Image" width="400"/>
</div>
  
## Contexto  
Você foi alocado(a) em um time da Indicium que está colaborando com um cliente no desenvolvimento de uma plataforma de aluguéis temporários na cidade de Nova York. O objetivo do cliente é estruturar uma estratégia de precificação baseada em análises dos dados de um grande concorrente.  

### Objetivo do Desafio  
Desenvolver um modelo preditivo de preços utilizando os dados fornecidos, realizando também uma análise exploratória que identifique padrões e insights relevantes.  

---

## Entregas  
O desafio está estruturado em três principais entregas:  

### 1. **Análise Exploratória de Dados (EDA)**  
Realizar uma análise detalhada para entender as características das variáveis, levantando hipóteses de negócio relevantes.  

#### Perguntas norteadoras:  
- Qual o local mais indicado para investir em um imóvel para alugar?  
- O número mínimo de noites e a disponibilidade ao longo do ano impactam o preço?  
- Existe algum padrão no texto do nome do local para imóveis de maior valor?  

---

### 2. **Modelagem Preditiva de Preços**  
Explicitar as etapas e escolhas envolvidas no processo de criação do modelo:  
- **Variáveis e transformações utilizadas:** Quais foram as selecionadas e por quê?  
- **Tipo de problema:** Regressão ou classificação? Justificar a escolha.  
- **Modelo utilizado:** Qual foi o modelo mais adequado? Discutir seus prós e contras.  
- **Métricas de avaliação:** Qual métrica foi usada e por que ela é a mais adequada para o problema?  

---

### 3. **Reprodutibilidade do Ambiente**  
Para facilitar a execução dos códigos, crie e ative o ambiente virtual com os seguintes comandos:  
```bash
conda create --name indicium  
conda activate indicium  
pip install -r requirements.txt  
```  

---

## Estrutura do Repositório  
```plaintext
📂 desafio-indicium
├── 📁 data                # Dados fornecidos para o desafio  
├── 📁 models              # Modelos treinados e scripts relacionados  
├── 📄 main.ipynb          # Jupyter notebook com a análise exploratória e modelagem  
├── 📄 README.md           # Documentação do projeto 
└── 📄 requirements.txt    # Dependências necessárias para execução do projeto  
```  

---

## Ferramentas Utilizadas  
- **Linguagem:** Python  
- **Principais bibliotecas:**  
  - `pandas`
  - `numpy` 
  - `matplotlib`
  - `seaborn` 
  - `scikit-learn`
 

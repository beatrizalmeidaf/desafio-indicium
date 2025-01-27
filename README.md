# Desafio Técnico - Cientista de Dados 🚀  
**Programa Lighthouse - Indicium**  

<div align="center">  
  <img src="https://github.com/user-attachments/assets/c8b636a6-9475-4ddb-8bd9-f9f80da3c424" alt="Image" width="400"/>  
</div>  

---

## 📌 Primeira Etapa: Consulte o Relatório Final  
O ponto principal desse desafio é o relatório das análises realizadas. Ele apresenta as descobertas, insights e justificativas das escolhas feitas ao longo do processo. Para entender as análises de forma mais aprofundada consulte os códigos desse repositório.

📄 **[Acesse o Relatório Final Aqui](https://github.com/beatrizalmeidaf/desafio-indicium/tree/main/relatorio/LH_CD_BEATRIZALMEIDAFELICIO.pdf)**  

---

## Contexto  
Você foi alocado(a) em um time da Indicium que está colaborando com um cliente no desenvolvimento de uma plataforma de aluguéis temporários na cidade de Nova York. O objetivo do cliente é estruturar uma estratégia de precificação baseada em análises dos dados de um grande concorrente.  

---

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

> **Nota:** As cores utilizadas nos gráficos desta análise foram cuidadosamente escolhidas para refletir a identidade visual da Indicium, garantindo coerência estética e comunicacional.  

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
```markdown  
📂 desafio-indicium  
├── 📁 data                             # Dados fornecidos para o desafio  
├── 📁 functions                        # Contém as implementações e códigos auxiliares para a execução principal do projeto  
    ├── 📁 analise_exploratoria         # Contém implementações auxiliares da análise exploratória de dados  
    ├── 📁 analises_perguntas_desafio   # Funções dedicadas à análise detalhada das questões e requisitos do desafio 
    ├── 📁 transformacoes               # Contém as principais transformações do desafio 
├── 📁 model                            # Modelo salvo em .pkl  
├── 📁 relatorio                        # Pasta onde está armazenado o relatório das análises  
├── 📄 main.ipynb                       # Jupyter notebook principal  
├── 📄 README.md                        # Documentação do projeto  
└── 📄 requirements.txt                 # Dependências necessárias para execução do projeto  
```  

---

## Ferramentas Utilizadas  

- **Linguagem:** Python  
- **Principais bibliotecas:**  
  - pandas  
  - numpy  
  - matplotlib  
  - seaborn  
  - scikit-learn  
  - statistics  
  - category_encoders  
  - folium   
  - pickle  
- **Versionamento:** Git  


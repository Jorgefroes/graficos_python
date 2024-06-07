import pandas as pd
import plotly.express as px

dados = pd.read_excel('vendas.xlsx')

#Verificando as primeiras e últimas linhas

#Entrada
dados.head()

dados.tail()

#Quantidades de linhas e collunas

#Entrada
dados.shape

#Informação sobre as colunas

#Entrada
dados.info()

#Juntando colunas

dados[["loja", "cidade"]]


#Gerando as estatísticas, agora vamos gerar algumas estatísticas importantes sobre a coluna preço

dados.describe()

#Obtendo os valores únicos de uma coluna

dados['loja'].unique()

#Armazenando valores a uma variavel sobre informações de uma coluna contando seus valores 

loja = dados['loja'].value_counts()
print(loja)

#Agrupando dados: O método groupy() realiza o agrpamento de dados por determinada coluna.
# sum() para soma
#mean para média

agrupamento = dados.groupby(['loja', 'estado', 'cidade', 'forma_pagamento'])['preco'].sum().to_frame()
print(agrupamento)

#Gráficos interativos

grafico = px.histogram(dados, x='loja',
                       y='preco',
                       color='forma_pagamento',
                       text_auto=True,
                       title='Faturamento por loja')
grafico.show()

lista_coluns = ['loja', 'cidade', 'estado', 'tamanho', 'local_consumo']
for coluna in lista_coluns:
    grafico = px.histogram(dados, x=coluna,
                           y='preco',
                           text_auto=True,
                           title='Faturamento',
                            color='forma_pagamento')
    grafico.show()
    grafico.write_html(f'Faturamento-{coluna}.html')



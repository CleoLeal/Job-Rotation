'''
    Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, 
faça um programa, na linguagem que desejar, que calcule e retorne:
    • O menor valor de faturamento ocorrido em um dia do mês;
    • O maior valor de faturamento ocorrido em um dia do mês;
    • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
'''
#biblioteca para a leitura de json
import json

# Função para ler o arquivo JSON
def ler_arquivo_json():
    arq = 'faturamento.json' 
    #abrindo arquivo
    with open(arq, 'r') as arquivo:
        #salvando dados
        dados = json.load(arquivo)
    #retornando dados
    return dados

#extraido os valores
def ExtrairDados(dados):
    #vetores para salvar os dados
    valores_faturamento = []
    for i in dados['faturamento_diario']:
        valores_faturamento.append(i['valor'])        
    return valores_faturamento

def Regras(valores):

    #filtrando os dados
    valores_filtrado = [valor for valor in valores_faturamento if valor != 0]

    #calculando a media
    media = round(sum(valores_filtrado)/len(valores_filtrado))
    #menor valor do json
    menor = min(valores_filtrado)
    print(f"O menor valor: {menor} ")

    #maior valor do json
    maior = max(valores_filtrado)
    print(f"O maior valor: {maior} ")

    #variável para calcular os dias
    dias = 0
    #contando os dias
    for i in valores:
        if i > media:
            #somandos
            dias += 1
    #retorno dos dias
    print(f'Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {dias}')

# pegando os dados
dados_faturamento = ler_arquivo_json()
valores_faturamento= ExtrairDados(dados_faturamento)

#mostrando os resultados
Regras(valores_faturamento)



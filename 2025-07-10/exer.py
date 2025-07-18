
import os,csv
from datetime import datetime
# Obtendo o diretorio onde o programa esta salvo
strDir = os.path.dirname(__file__)
# Inicializando a lista para armazenar os dados
cotacoes = []
# Abrindo e lendo o arquivo
try:
    
    with open(f'{strDir}\\cotacao_dolar.csv', 'r', encoding='utf-8') as arqLeitura:
        leitor = csv.reader(arqLeitura, delimiter=';')
        # Ignorando o cabeçalho
        next(leitor)
        
        for linha in leitor:
            # Convertendo os dois primeiros valores para float e o terceiro para data
            cotacao_compra = float(linha[0].replace(',', '.'))
            cotacao_venda = float(linha[1].replace(',', '.'))
            data_hora_cotacao = datetime.strptime(linha[2], '%d/%m/%Y')
            # Adicionando os dados à lista
            cotacoes.append([cotacao_compra, cotacao_venda, data_hora_cotacao])

except FileNotFoundError:
    print('Erro: arquivo não encontrado')
except Exception as erro:
    print(f'Erro: {erro}')
# Exibindo os dados processados
for cotacao in cotacoes:
    print(cotacao)
    
    
    
    
'''
  1) A partir do conteúdo do arquivo cotacao_dolar.csv gerar uma lista onde cada item
      dessa lista será uma sub-lista com os valores de cada linha do arquivo.

      a) Os valores estão separados por ";";
      b) Os dois primeiros valores são valores do tipo FLOAT;
      c) O terceiro valor é do tipo DATE;
      '''
      
from datetime import datetime

listaCotacao = []

with open("cotacao_dolar.csv", "r", encoding="utf-8") as arquivo:
     for linha in arquivo:
        valores = linha.strip().split(";")
        if len(valores) < 3:
             continue 
        try:
            valor1 = float(valores[0])
            valor2 = float(valores[1])
            data = datetime.strptime(valores[2], "%Y-%m-%d").date()
            listaCotacao.append([valor1, valor2, data])
        except ValueError:
            continue  # ignora linhas com dados mal formatados

print(listaCotacao)
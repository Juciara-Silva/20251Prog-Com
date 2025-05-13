import sys

try:
    intDividendo = int(input('Digite o dividendo: '))
    intDivisor = int(input('Digite o dividendo: '))
    fltResultado = intDividendo /  intDivisor

except ValueError:
    print('ERRO: informe um valor que possa ser convertido em Inteiro.')
except ZeroDivisionError:
    print('ERRO: Não existe divisão por zero.')
except Exception as tipoExcecao:
    print(f'ERRO: {tipoExcecao}') #apaga esse porque o de baixo já generalizado para mostrar todos os erros
    print(f'ERRO: {sys.exc_info()}') # esse é o de baixo
else:
    print(fltResultado) 


import sys

try:
    x = int(input('Digite o primeiro número inteiro positivo: '))
    y = int(input('Digite o segundo número inteiro positivo: '))

    if x <= 0 or y <= 0:
        sys.exit('Informe apenas valores inteiros positivos')

    resultado = 0
    contador = 0
    expressao = ""

    while contador < y:
        resultado += x
        expressao += f"{x} + " if contador < y - 1 else f"{x}" 
        contador += 1

    print(f'{expressao}, totalizando {resultado}.')

except ValueError:
    sys.exit('Informe apenas valores inteiros positivos')
except Exception as e:
    sys.exit(f'erro: {e}')
'''
y é quantas vezes x vai ser repetido
'''
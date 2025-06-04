'''
   Dados dois números inteiros positivos, determinar o Máximo Divisor 
   Comum (MDC) entre eles usando o Algoritmo de Euclides.
'''

import sys

try:
    
    mdc1 = int(input('Informe o primeiro MDC '))
    mdc2 = int(input('Informe o segundo MDC '))
    
    if mdc1 <= 0 or mdc2 <= 0:
        sys.exit('Erro Informe o multiplicador e o multiplicando positivo')
    
    for _ in range(mdc2):  
        resto = mdc1 % mdc2  
        mdc1 = mdc2  
        mdc2 = resto  
        if mdc2 == 0:  
            break   
        print(f'O MDC é {mdc1}')

except ValueError:
    sys.exit('Erro: Não foi informado um valor inteiro valido')
except Exception as e:
    sys.exit(f'Erro:{e}')
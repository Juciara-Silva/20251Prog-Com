'''
   Dados dois números inteiros positivos, determinar o Máximo Divisor 
   Comum (MDC) entre eles usando o Algoritmo de Euclides.
'''

import sys

try:
    
    mdc1 = int(input('Informe o primeiro numero '))
    mdc2 = int(input('Informe o segundo numero '))
    
    if mdc1 <= 0 or mdc2 <= 0:
        sys.exit('Erro Informe o multiplicador e o multiplicando positivo')
    
    for i in range(mdc2):  
        if mdc2 == 0:  
            break   
        resto = mdc1 % mdc2  
        mdc1 = mdc2  #o valor do segundo é substituido pelo primeiro
        mdc2 = resto  #e o segundo passa ser o resto
        
       
    print(f'O MDC é {mdc1}')

except ValueError:
    sys.exit('Erro: Não foi informado um valor inteiro valido')
except Exception as e:
    sys.exit(f'Erro:{e}')
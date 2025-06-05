'''
   A sequência de Fibonacci é uma sequência numérica onde cada número 
   é a soma dos dois anteriores, com os dois primeiros números sendo 1 e 1. 

   Implemente um programa que receba um número inteiro n e retorne os n 
   primeiros termos da sequência de Fibonacci.
'''

import sys

try:
    
    fib = int(input('Informe o primeiro numero '))

    
    if fib <= 0:
        sys.exit('Erro Informe o numero inteiro positivo')
    
    
    for i in range(fib +fib ):  
 
        num = fib + fib  
        res = fib + num  
        break  
       
    print(f'a seguencia é {res}')

except ValueError:
    sys.exit('Erro: Não foi informado um valor inteiro valido')
except Exception as e:
    sys.exit(f'Erro:{e}')

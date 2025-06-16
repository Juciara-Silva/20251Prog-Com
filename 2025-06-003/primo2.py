'''
   Os primeiros dois números consecutivos que podem ser decompostos 
   como apenas dois fatores primos são 14 = (2 * 7) e 15 = (3 * 5).

   Faça um programa que recebe a quantidade n de fatores primos que 
   um número pode ter. 
   
   O programa deve listar os primeiros n números consecutivos que 
   atendem ao critério.
'''

import sys

try:
    
    primo = int(input('Informe a quantidade de fatores primos que um numero pode ter:'))

    
    if primo <= 1:
        sys.exit('Erro Informe um numero maior que um')
    
    cont = 0
    
    for i in range(primo ):  
     resto = primo % (i+1) # primo dividido por cada numero que for passando o +1 é para não começar do 0 e sim do 1
     if resto == 0:
         cont = cont + 1

     
    print(f' {cont} numero de divisores')

    if cont == 2:
     print(f' {primo} primo')
    else:
     print(f' {primo} não primo') 

except ValueError:
    sys.exit('Erro: Não foi informado um valor inteiro valido')
except Exception as e:
    sys.exit(f'Erro:{e}')




import sys

try:
    num = int(input('Informe um numero '))
except ValueError:
    sys.exit('erro: informe um numero inteiro valido')
except Exception as e:
    sys.exit(f'erro: {e}')
else:
    if num < 0:
        sys.exit('ERRO: Não existe fatorial para números negativos ...')
    if num < 2:
       sys.exit(f'{num}! = 1')
       ''' 
    fatorial = num
    auxiliar = num -1
       
    while auxiliar >= 2:
           fatorial *= auxiliar
           auxiliar -= 1
           print(f'{num}! = {fatorial}')
           '''
    '''explicação do que esta entre () se num for igual a 3 vai 
              ficar o numero num-1 significa onde começã no caso se for 3 vai começar pelo 2, o 1 é onde 
              ele define onde para a seguencia vai ate o 2 e o -1 é porque ele vai diminuindo -1 e não aumentando
           '''
    for auxiliar in range (num -1, 1, -1 ):
     num *= auxiliar
     print(f'{num}! = {num}')
               
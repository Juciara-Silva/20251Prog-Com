

import sys

try:
    num = int(input('Infforme um numero '))
except ValueError:
    sys.exit('erro: informe um numero inteiro valido')
except Exception as e:
    sys.exit(f'erro: {e}')
else:
    if num < 0:
        sys.exit('ERRO: Não existe fatorial para números negativos ...')
    if num < 2:
       sys.exit(f'{num}! = 1')
       
    fatorial = num
    auxiliar = num -1
       
    while auxiliar >= 2:
           fatorial *= auxiliar
           auxiliar -= 1
           print(f'{num}! = {fatorial}')
           
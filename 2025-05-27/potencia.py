
import sys

try:
   
   
   base = int(input('Informe a base: '))
   potencia = int(input('Informe a potencia: '))
   
   if base <= 0 or potencia <= 0:
       sys.exit('Informe base e potencia positiva')
   
   
   resultado = 1
   contador = 1 
   while contador <= potencia:
       resultado *= base
       contador += 1
       
   print(f'{base} ** {potencia} = {resultado}' )   
    
except ValueError:
    sys.exit('ERRO: Não foi informado um valor inteiro válido...')

except Exception as e:
    sys.exit(f'ERRO: {e}')
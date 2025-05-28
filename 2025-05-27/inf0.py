
import sys


valor = None



try:
    num = int(input('Digite números inteiros : '))
    
    if num < 0:
        sys.exit('Informe apenas valores inteiros ')



    else:
     num == 0
    sys.exit('Fim ')



    
except ValueError:
    sys.exit('Informe apenas valores inteiros positivos')
except Exception as e:
    sys.exit(f'erro: {e}')

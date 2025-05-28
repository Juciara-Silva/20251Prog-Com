
import sys

try:
    intMultiplicador = int(input('Digite um multiplicador da tabuada: '))
    if intMultiplicador <= 0:
        sys.exit('Informe um valor inteiro positivo')
except ValueError:
    sys.exit('Informe um valor inteiro positivo')

intnumero = 1
while intnumero <= 10:
    print(f'{intMultiplicador} x {intnumero} = {intMultiplicador * intnumero}')
    intnumero += 1


import sys

v = int(input('Digite o valor de velocidade inicial:'))
if v <= 0:
 sys.exit('Informe uma velocidade positiva')


a = int(input('Digite o valor de aceleração:'))
if a <= 0:
 sys.exit('Informe uma aceleração positiva')


t = int(input('Digite o valor de tempo:'))
if t <= 0:
 sys.exit('Informe um tempo positiva')


distancia = v * t + ( a*t ** 2 / 2 )

print(f'A distancia percorrida é de {distancia}')


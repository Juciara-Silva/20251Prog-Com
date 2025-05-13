
#programa para classificar um triangulo quanto aos angulos.
#o programa devera solicitar 3 angulos interiros positivos;
#para ser um triangulo,a soma dos angulos devera ser igua a 180;
#retangulo: possui um angulo interno reto igual a 90.
#obtusangulo: possui um angulo interno obtuso maior que 90
#acutangulo: possui todos os angulos internos agudos menores que 90


import sys

#informe o primeiro angulo 
angulo1 = int(input('informe um angulo inteiro positivo:'))
if angulo1 <= 0 :
    sys.exit('erro: angulo 1 invalida. um angulo inteiro positivo')

#informe o segundo angulo 
angulo2 = int(input('informe o segundo angulo inteiro positivo:'))
if angulo2 <= 0 :
    sys.exit('erro: angulo 2 invalida. infome um angulo inteiro positivo')

#informe o terceiro angulo 
angulo3 = int(input('informe o terceiro angulo inteiro positivo:'))
if angulo3 <= 0:
    sys.exit('erro: angulo 3 invalida. infome um angulo inteiro positivo')

if angulo1 + angulo2 = angulo3 != 180:
    sys.exit('erro: A soma dos angulos deve ser 180.')

angulo = int(round(angulo1+angulo2+angulo3))



if angulo == 90:
    print('triangulo retangulo.')
elif angulo > 90:
    print('triangulo obtusangulo.')
elif angulo < 90:
    print('triangulo ocutangulo.')





if angulo == 90:
    print('triangulo retangulo.')
elif angulo > 90:
    print('triangulo obtusangulo.')
elif angulo < 90:
    print('triangulo ocutangulo.')
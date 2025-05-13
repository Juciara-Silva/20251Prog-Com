
#programa para classificar um triangulo quanto aos angulos.
#o programa devera solicitar 3 angulos interiros positivos;
#para ser um triangulo,a soma dos angulos devera ser igua a 180;
#retangulo: possui um angulo interno reto igual a 90.
#obtusangulo: possui um angulo interno obtuso maior que 90
#acutangulo: possui todos os angulos internos agudos menores que 90


import sys

#informe a nota da etapa um
angulo1 = int(input('informe um angulo inteiro positivo:'))
if etapa1 < 0 and etapa1 >100:
    sys.exit('erro: angulo 1 invalida. um angulo inteiro positivo')

#informe a nota da etapa dois
angulo2 = int(input('informe o segundo angulo inteiro positivo:'))
if etapa2 < 0 and etapa2 >100:
    sys.exit('erro: angulo 2 invalida. infome um angulo inteiro positivo')

angulo3 = int(input('informe o terceiro angulo inteiro positivo:'))
if etapa3 < 0 and etapa3 >100:
    sys.exit('erro: angulo 3 invalida. infome um angulo inteiro positivo')

angulo = int(round(angulo1+angulo2+angulo3))

if angulo == 90:
    print('triangulo retangulo.')
elif angulo > 20:
    print('angulo obtusangulo.')
elif angulo < 90:
    print('Aluno reprovado.')
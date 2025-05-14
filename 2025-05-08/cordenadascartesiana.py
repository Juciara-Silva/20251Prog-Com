'''
   Programa para informar em qual quadrante cartesiano o ponto está.

   - O programa deverá solicitar as duas coordenadas (x,y) de um ponto;

   - O ponto está no 1º quadrante quando X e Y forem positivos;
   - O ponto está no 2º quadrante quando X for negativo e Y for positivo;
   - O ponto está no 3º quadrante quando X e Y forem negativos;
   - O ponto está no 4º quadrante quando X for positivo e Y for negativo;
'''

coodX = float(input('Digite a coordenada X:'))
coody = float(input('Digite a coodernada y:'))

if coodX > 0 and coody > 0:
    print('O ponto esta no primeiro quadrante')

elif coodX < 0 and coody > 0:
    print('o ponnto esta  no segundo quadrante')

elif coodX < 0 and coody < 0:
    print('o ponto esta no terceiro quadrante')

elif coodX > 0 and coody < 0:
    print('o ponto esta no quarto quadrante')

else:
    print ('o ponto esta na origem ou nos eixos das coodernadas.')
import sys


d= int(input('Informe a distancia entre lajes e Natal em km:'))
if d <= 0:
 sys.exit('Informe uma distancia maior que zero ')


v = int(input('Informe a velocidade inicial do carro em km/h:'))
if v <= 0:
 sys.exit('Informe uma velocidade maior que zero ')


a= int(input('Informe a aceleração do carro em metro por segundo ao quadrado:'))
if a <= 0:
 sys.exit('Informe uma distancia maior que zero ')

d = d*1000 
v = v/3.6

delta = v**2-4*a*d
if d < 0:
 sys.exit('Não é possivel calcular o tempo ')

#b na raiz quadrada é a velocidade inicial
 t= (-v + delta ** 0.5) / (2*a)


 #agora t vai ser tranformar em hora porque ta em segndo

hora = t//3600
t=t%3600
minuto = t // 60
segundo = t % 60

print(f' tempo = {hora}:{minuto}:{segundo}')


d= float(input('Informe a distancia entre lajes e Natal em km/h:'))
v = float(input('Informe a velocidade inicial do carro em km/h:'))
a= float(input('Informe a aceleração do carro em metro por segundo ao quadrado:'))

t =   (a*t**2//2) + v * t - d 
hora_formatada = hora_atual.strftime("%H:%M:%S")

print(f'A distancia percorrida é de {t}')







from datetime import datetime

# Obtendo a hora atual
hora_atual = datetime.now()

# Formatando para hh:mm:ss
hora_formatada = hora_atual.strftime("%H:%M:%S")

print("Hora formatada:", hora_formatada)
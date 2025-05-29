import sys

try:
    
    Multiplicador = int(input('Informe o multiplicador'))
    Multiplicando = int(input('Informe o multiplicando'))
    
    if Multiplicador <= 0 or Multiplicando <= 0:
        sys.exit('Erro Informe o multiplicador e o multiplicando positivo')
       
    resultado = 0
    contando = 1
    while contando <= Multiplicador:
        resultado += Multiplicando
        contando += 1
           
    print(f'{Multiplicador} x {Multiplicando} = {resultado}')
    

except ValueError:
    sys.exit('Erro: Não foi informado um valor inteiro valido')
except Exception as e:
    sys.exit(f'Erro:{e}')
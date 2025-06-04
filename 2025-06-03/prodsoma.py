import sys

try:
    
    Multiplicador = int(input('Informe o multiplicador '))
    Multiplicando = int(input('Informe o multiplicando '))
    
    if Multiplicador <= 0 or Multiplicando <= 0:
        sys.exit('Erro Informe o multiplicador e o multiplicando positivo')
        ''' 
    resultado = 0
    contando = 1
    while contando <= Multiplicador:
        resultado += Multiplicando
        contando += 1
           '''
           
    '''
          Multiplicador: Indica quantas vezes o multiplicando será somado. Exemplo: Se o multiplicador for 4, significa que o número será somado 4 vezes.
          Multiplicando: É o número que será somado repetidamente. Exemplo: Se o multiplicando for 3, ele será adicionado a cada rodada.
          Se multiplicador = 4 e multiplicando = 3, o cálculo acontece assim: ➡ 3 + 3 + 3 + 3 = 12  Isso equivale a 4 × 3 = 12.
           '''
           
  
    resultado = 0       
    for contando in range ( Multiplicador):
          resultado += Multiplicando
    print(f'{Multiplicador} x {Multiplicando} = {resultado}')
  

except ValueError:
    sys.exit('Erro: Não foi informado um valor inteiro valido')
except Exception as e:
    sys.exit(f'Erro:{e}')
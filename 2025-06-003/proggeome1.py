'''
   Dado que uma Progressão Geométrica (P.G.) é a uma sequência numérica 
   cujo quociente (q) ou razão entre um número e outro (exceto o primeiro) 
   é sempre igual. Vale lembrar que essa razão é sempre constante e pode 
   ser qualquer número racional (positivos, negativos, frações) exceto o 
   número zero (0).

   Faça um programa que:
      a) Solicite ao usuário um valor inteiro inicial e a razão da P.G.;
      b) Solicite um novo valor inteiro positivo correspondente a quantidade 
         de elementos da PG e exiba os valores dessa P.G.;
      c) Informe se a P.G. é constante, oscilante, crescente ou decrescente;
      d) Calcule a soma dos elementos dessa P.G.;
      e) Solicite um outro valor inteiro n correspondente a enésima posição 
         de um elemento da P.G. e exibir o valor desse elemento.
'''



import sys

try:
    
    prog = int(input('Informe o primeiro termo '))
    razao = int(input('Informe a razão '))
    seg = int(input('Informe quantas seguencias vc vai querer'))

    if razao == 0:
       sys.exit('Erro: A razão da PG não pode ser zero.')
    
    if seg <= 0:
            sys.exit('Erro: A quantidade de elementos deve ser um número inteiro positivo.')

    for i in range(seg):
     termo = prog * (razao ** i)  # Fórmula da P.G.
    print(f'a pg é {termo}')
       
    '''ex: 2 vezes 3 elevado a 0 = 2 ; 2 vezes 3 elevado a 1 = 6  e asim por diante
    ate acabar a seguencia '''
    if razao == 1:
     print(' constante')
    elif razao > 1:
     print('crescente') 
    elif 0 < razao < 1:
     print('decrescente') 
    elif razao < 0:
     print('oscilante ') 
    else:
     print("Razão inválida.")
except ValueError:
    sys.exit('Erro: Não foi informado um valor inteiro valido')
except Exception as e:
    sys.exit(f'Erro:{e}')

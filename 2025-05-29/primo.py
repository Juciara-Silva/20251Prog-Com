import sys

try:
    # Solicita um número inteiro ao usuário
    valor = int(input('Informe um número inteiro: '))

    # Verifica se o número é positivo
    if valor <= 0:
        sys.exit('Erro: Informe um número inteiro positivo.')

except ValueError:
    sys.exit('Erro: Não foi informado um valor inteiro válido.')
except Exception as e:
    sys.exit(f'Erro: {e}')
    
else:
    # Inicializa os contadores
    intCntdiv = 1  # Começa contando que 1 é um divisor
    intDivisor = 2  # Começa verificando a partir do número 2

    while intDivisor <= valor:
        if valor % intDivisor == 0:
            intCntdiv += 1  # Conta os divisores encontrados
        intDivisor += 1  # Incrementa para testar o próximo número
        '''
        organizar esse codigo para verificar quando 
        passar de 2 divisores parar de rodar sem precisar verificar todos
        if intEntdiv > 2
        break
    '''
    
    
    # Se o número tiver apenas dois divisores (1 e ele mesmo), é primo
    if intCntdiv == 2:
        print(f'{valor} é primo!')
    else:
        print(f'{valor} não é primo.')

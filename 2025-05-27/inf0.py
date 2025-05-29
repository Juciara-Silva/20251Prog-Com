import sys

valor = None
somapositivos = 0
qtdvalor = 0
qtdvalpositivo = 0

while valor != 0:
    try:
        valor = int(input('Informe um valor inteiro: '))

        if valor > 0:
            somapositivos += valor
            qtdvalpositivo += 1

        if valor != 0: 
            qtdvalor += 1

    except ValueError:
        sys.exit('Informe apenas valores inteiros positivos')
    except Exception as e:
        sys.exit(f'Erro: {e}')


print(f'Quantos números inteiros foram digitados: {qtdvalor}')
print(f'Soma dos números inteiros positivos: {somapositivos}')
print(f'Média dos números inteiros positivos: {somapositivos / qtdvalpositivo}')

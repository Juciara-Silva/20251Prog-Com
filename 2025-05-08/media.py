'''
   Programa para calcular a média de uma disciplina
   semestral no IFRN.

   As notas devem ser inteiras e entre 0 e 100 (inclusive).

   Caso a média seja igual ou superior a 60 o aluno estará
   Aprovado; Caso a média seja igual ou superior a 20 o aluno
   estará em Prova Final e os demais casos o aluno estará Reprovado. 
'''




import sys

#informe a nota da etapa um
etapa1 = int(input('informe a nota da etapa 1:'))
if etapa1 < 0 or etapa1 >100:
    sys.exit('erro: Nota etapa 1 invalida. infome nota entre 0 e 100')

#informe a nota da etapa dois
etapa2 = int(input('informe a nota da etapa 2:'))
if etapa2 < 0 or etapa2 >100:
    sys.exit('erro: Nota etapa 2 invalida. infome nota entre 0 e 100')

    #calculando a media
media = int( round((etapa1 * 2 + etapa2 * 3)/5,0))
print(f'Media do Aluno:{media}')#não aceita os quebrados
print(f'Media do Aluno:{media:.0f}')#aceita os quebrados

#verificando a situação do aluno
if media >= 60:
    print('Aluno aprovado.')
elif media >= 20:
    print('Aluno prova final.')
else:
    print('Aluno reprovado.')
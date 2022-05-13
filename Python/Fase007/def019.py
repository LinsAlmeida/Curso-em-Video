from random import choice
a1 = input('Digite o Nome do primeiro aluno: ')
a2 = input('Digite o Nome do segundo aluno: ')
a3 = input('Digite o Nome do terceiro aluno: ')
a4 = input('Digite o Nome do Quarto aluno: ')

lista = [a1, a2 ,a3, a4]

escolhido = choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))
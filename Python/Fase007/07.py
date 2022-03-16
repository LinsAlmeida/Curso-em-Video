n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))
soma = n1 + n2
multi = n1 * n2
div = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma {}, \n o produto {} \n e a divisão {:.3f}'.format(soma, multi, div), end='')
print ('Divisão inteira {} \n e a potencia {}'.format(di, e))
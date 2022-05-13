form math import hypot
catetoOP = float(input('Comprimento do cateto oposto: '))
catetoAD = float(input('Comprimento do cateto adjacente: '))
hi = hypot(catetoOP, catetoAD)
print (' A hipotenusa vai medir {:.2f}'.format(hi))
'''Metodo utilizando a importação '''

'''
catetoOP = float(input('Comprimento do cateto oposto: '))
catetoAD = float(input('Comprimento do cateto adjacente: '))
hi = (catetoOP ** 2 + catetoAD ** 2) ** (1/2)
print ('A hipotenusa vai medir {:.2f}'.format(hi))
Metodo matematico 
'''
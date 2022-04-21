dias =int(input('Quantos dias alugados?'))
km = float(input('Quabntos Km Rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a apgar é de R${:.2f}'.format(pago))
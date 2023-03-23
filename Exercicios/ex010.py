# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

v = float(input('Digite quanto você possui na carteira em R$'))
# d = 5.28
c = v / 5.28
print('O valor que você terá em dólar é igual a ${:.2f}'.format(c))
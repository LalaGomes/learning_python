# Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input('Digite seu salário:'))

p = s * 0.15 + s
# p = s + (s * 15 / 100)

print('Seu novo salário será {:.2f}'.format(p))
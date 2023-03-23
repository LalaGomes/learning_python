# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
C = float(input('Entre com a temperatura em graus Celsius:'))

F = C * (9/5) + 32
# f = ((9 * C) / 5) + 32

print('Valor em Fahrenheit: {0}°F'.format(F))
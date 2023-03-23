#  Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos kms foram percorridos?'))
d = int(input('Quantos dias foram alugados?'))
pago = (d * 60) + (km * 0.15)
print('O preço a pagar por {}km rodados será R${:.2f}'.format(km,pago))
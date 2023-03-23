# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-lo, sabendo que cada litro de tinta, pintar uma área de 2m^2.

largura = float(input('Insira a largura da parede em metros:'))
altura = float(input('Insira a altura da parede em metros:'))

area = largura * altura
tinta = area / 2
print('A quantidade de tinta para pintar {} metros será {} litros'.format(area,tinta))

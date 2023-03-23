# Faça um programa que leia um nùmero inteiro qualquer e mostre na tela a sua tabuada

tabuada = int(input('Digite um número:'))

for count in range(10): 
    print('%d x %d = %d' % (tabuada, count+1, tabuada*(count+1)))

# print('{} x {} = {}'.format(tabuada, 1, tabuada * 1))    
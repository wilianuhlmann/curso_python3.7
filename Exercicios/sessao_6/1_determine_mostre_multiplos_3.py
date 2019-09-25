"""
Faça um programa que determine e
mostre os cinco primeiros multiplos de 3, considerando numeros maiores que 0.
"""
# Esta errado essa merda.
cont = 0
multiplo = int(input("Digite um numero para ver o multiplo: "))
for multiplo in range(1, 100):
    cont = cont + 1
    if num > 0:
        if cont < 5:
            break
            num = (num * multiplo)
            print(num)



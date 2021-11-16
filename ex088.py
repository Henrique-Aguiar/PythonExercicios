from random import randint
from time import sleep
print('-'*40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-'*40)
lista = []
jogos = []
tot = 1
njg = int(input('Quantos jogos você quer que eu sorteie? '))
while tot <= njg:
    cont = 0
    while True:
        num = randint(0, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    tot += 1
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
print('-='*3, f'SORTEANDO {njg} JOGOS', '-='*3)
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i+1}: {l}')

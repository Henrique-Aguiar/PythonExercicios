from random import randint
from time import sleep
computador = randint(0, 5) #Faz o comutador "pensar"
print('-=-'*20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar... ')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? ')) #O jogador tenta adivinhar
print('PROCESSANDO... ')
sleep(2)
if computador == jogador:
    print('PARABÉNS! Você conseguiu me vencer! ')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}')

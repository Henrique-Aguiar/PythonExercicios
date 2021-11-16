from random import randint
print('''Sou seu computador...
Acabei de pensar em um numero entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
computador = randint(1, 10)
palpites = 0
jogador = 0
while jogador != computador:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador < computador:
        print('Mais... Tente mais uma vez.')
    elif jogador > computador:
        print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')


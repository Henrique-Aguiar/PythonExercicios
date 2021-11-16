def ficha(j='<desconhecido>', gol=0):
    print('-' * 30)
    print(f'O jogador {j} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do jogador: '))
g = str(input('Números de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)

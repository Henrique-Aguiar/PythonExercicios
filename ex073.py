times = ('Atletico-MG', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Bragantino', 'Corinthians',
         'Fluminence', 'Cuiabá', 'Internacional', 'Atletíco-GO', 'Athletico-PR', 'Ceará SC',
         'Santos', 'Juventude', 'Bahia', 'São Paulo', 'América-MG', 'Grêmio', 'Sport Recife', 'Chapecoense')
print('-='*15)
print(f'Lista de times do Brasileirão: {times}')
print('-='*15)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-='*15)
print(f'Os 4 últimos são: {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
print('-='*15)
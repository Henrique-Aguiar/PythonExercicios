nome = str(input('Digite seu nome completo: ')).strip()
n = nome.title().split()
print('Muito prazer em te conhecer! ')
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu último nome é {n[len(n)-1]}')


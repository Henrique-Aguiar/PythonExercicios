ficha = {}
lista = []
soma = media = 0
while True:
    ficha.clear()
    ficha['nome'] = str(input('Nome: '))
    while True:
        ficha['sexo'] = str(input('Sexo: [M/F] ')).upper()
        if ficha['sexo'] in 'MF':
            break
        print('ERRO! Responda apenas M ou F.')
    ficha['idade'] = int(input('Idade: '))
    soma += ficha['idade']
    lista.append(ficha.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp in 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
media = soma / len(lista)
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastrdas foram: ', end='')
for p in lista:
    if p['sexo'] in 'F':
        print(p['nome'], end='. ')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')


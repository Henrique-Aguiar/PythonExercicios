n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a média do aluno é {média:.1f}')
if média < 5:
    print('O aluno está REPROVADO.')
#elif média >= 5 and média < 7:
elif 7 > média >= 5:
    print('O aluno está em RECUPERAÇÃO')
else:
    print('O aluno está APROVADO')

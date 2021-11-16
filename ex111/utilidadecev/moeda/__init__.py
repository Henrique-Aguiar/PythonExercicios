def metade(num=0, formato=False):
    p = num / 2
    return p if formato is False else moeda(p)


def dobro(num=0, formato=False):
    p = num * 2
    return p if formato is False else moeda(p)


def aumentar(num=0, porct=0, formato=False):
    p = num + num * porct / 100
    return p if formato is False else moeda(p)


def diminuir(num=0, porct=0, formato=False):
    p = num - num * porct / 100
    return p if not formato else moeda(p)


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')


def resumo(num=0, porct=10, porcent=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'{porct}% de aumento: \t{aumentar(num, porct, True)}')
    print(f'{porcent}% de redução: \t\t{diminuir(num , porcent, True)}')
    print('-' * 30)

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





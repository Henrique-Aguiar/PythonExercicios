def metade(num=0):
    p = num / 2
    return p


def dobro(num=0):
    p = num * 2
    return p


def aumentar(num=0, porct=0):
    p = num + num * porct / 100
    return p


def diminuir(num=0, porct=0):
    p = num - num * porct / 100
    return p


def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')





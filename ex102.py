def fatorial(n, show=False):
    """
    -> Calcular o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opicional) mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, True))

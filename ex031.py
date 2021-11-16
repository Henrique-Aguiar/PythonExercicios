distancia = float(input('Qual é a distancia da sua viajem? '))
print(f'Você esta prestes a começar uma viajem de {distancia:.1f}Km. ')
preco = distancia *0.5 if distancia < 200 else distancia*0.45
print(f'E o preço da sua passagem será de R${preco:.2f}')
'''if distancia < 200:
    preço = distancia*0.5
else:
    preço = distancia*0.45'''
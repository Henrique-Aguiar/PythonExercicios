peso = float(input('Qual a sua peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / altura**2
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso normal.')
elif imc < 25:
    print('PARABÉNS, você está com o peso ideal.')
elif imc < 30:
    print('Você está com sobrepeso.')
elif imc < 40:
    print('Você está em obesidade!')
else:
    print('Você está em obesidade morbida, CUIDADO!')

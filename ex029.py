v = float(input('Qual a velocidade atual do carro? '))
if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é 80Km/h')
    multa = (v-80)*7
    print(f'Você deve pagar uma multa de R${multa:.2f}')
    print('Tenha um bom dia! Dirija com segurança!')
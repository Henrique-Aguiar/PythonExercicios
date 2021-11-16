sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()
while sexo not in "MF":
    sexo = str(input('Dados invalido. Por favor, informe seu sexo: ')).upper().strip()
print(f'Sexo {sexo} registrado com sucesso')

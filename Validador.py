invalido = ['00000000000', '11111111111', '22222222222', '33333333333', '44444444444', '55555555555', '66666666666', '77777777777', '88888888888', '99999999999']

# 1º Passo - CPF tem que conter 11 digitos
while True:
    cpf = str(input('Digite o CPF que deseja consultar: '))
    if cpf.isnumeric():
        if len(cpf) != 11 or cpf in invalido:
            print('CPF invalido!')
        else:
             break
    else:
        print('Digite apenas numeros.!')

digito1 = int(cpf[9:10])
digito2 = int(cpf[10:])
verificador1 = 0
verificador2 = 0

### Validação do primeiro Digito
for i, v1 in zip(range(1, 10), range(10, 1, -1)):
    verificador1 = verificador1 + int(cpf[i - 1:i]) * v1
v1 = (11 - (verificador1 % 11))

if (v1 == 10) or (v1 == 11):
    v1 = 0
else:
    pass

if v1 == digito1:
    d1 = 0
    pass
else:
    d1 = 1

### Validação do segundo Digito
for i, v2 in zip(range(1, 11), range(11, 1, -1)):
    verificador2 = verificador2 + int(cpf[i - 1:i]) * v2
v2 = (11 - (verificador2 % 11))

if (v2 == 10) or (v2 == 11):
    v2 = 0
else:
    pass

if v2 == digito2:
        d2 = 0
        pass
else:
    d2 = 1

### Traz o resultado
if (d1 + d2 == 0):
    print('CPF Valido.')
else:
    print('CPF Invalido.')

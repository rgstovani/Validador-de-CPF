import PySimpleGUI as sg


layout = [
    [sg.Text('Digite o CPF:')],
    [sg.InputText(key='entrada_cpf')],
    [sg.Button('Consultar'), sg.Button('Cancelar')],
    [sg.Text(key='texto_saida')],
    [sg.Text(key='texto_saida2')]
]

janela = sg.Window('Validador de CPF', layout)

invalido = ['00000000000', '11111111111', '22222222222', '33333333333', '44444444444', '55555555555', '66666666666', '77777777777', '88888888888', '99999999999']

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break

    if evento == 'Consultar':
        janela['texto_saida'].update(f"O CPF digitado: {valores['entrada_cpf']}.")
        cpf = str(valores['entrada_cpf'])
        if cpf.isnumeric():
            if len(cpf) != 11 or cpf in invalido:
                pass
    else:
        janela['texto_saida2'].update('Não é um CPF Válido.')

    ### Validação do primeiro Digito
    digito1 = int(cpf[9:10])
    verificador1 = 0
    for i, v1 in zip(range(1, 10), range(10, 1, -1)):
        verificador1 += int(cpf[i - 1:i]) * v1
    v1 = (11 - (verificador1 % 11))
    if (v1 == 10) or (v1 == 11):
        v1 = 0
    else:
        pass

    ### Validação do segundo Digito
    digito2 = int(cpf[10:])
    verificador2 = 0
    for i, v2 in zip(range(1, 11), range(11, 1, -1)):
        verificador2 += int(cpf[i - 1:i]) * v2
    v2 = (11 - (verificador2 % 11))
    if (v2 == 10) or (v2 == 11):
        v2 = 0
    else:
        pass

    ### Verifica validade CPF
    if v1 == digito1:
        if v2 == digito2:
            janela['texto_saida2'].update('É um CPF Válido.')
        else:
            janela['texto_saida2'].update('Não é um CPF Válido.')
    else:
        janela['texto_saida2'].update('Não é um CPF Válido.')

janela.close()
while  True:

    num1 = input('Digite um numero: ')
    num2 = input('Digite um numero: ')
    op = input('Qual a operacao: ')

    num_valido = None
    num1_float = 0
    num2_float = 0
    try:
        num1_float = float(num1)
        num2_float = float(num2)
        num_valido = True
    except:
        num_valido = None

    if num_valido is None :
        print('Numero digitados nao sao validos')
        continue

    op_permitido = '+-/*'

    if  op not in op_permitido:
        print('Nao permido, operador invalido: ')

    if len(op) > 1:
        print('Digite apenas um operador:  ')
        continue


    if op == '+':
        print(num1_float + num2_float)
    elif op == '-':
        print(num1_float - num2_float)
    elif op == '/':
        print(num1_float / num2_float)
    elif op == '*':
        print(num1_float * num2_float)


    sair = input('Sair [S]im: ')
    sair = sair.lower()
    sair = sair.startswith('s')
    if sair  == 's' or 'S':
        break
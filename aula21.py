# no and, se qualquer valor for considerado falso, a expressão será avaliada como falsa

user = input('Digite o usuario: ')
senha = input('Digite a senha: ')

if user == 'ricardo' and senha == 'renato':
    print('Entrou!!!')
else:
    print('Senha incorreta!!!')    

print(True and False and True)
print(True and 4.5 and True)
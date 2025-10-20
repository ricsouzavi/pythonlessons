primeiro_val = input('Digite um valor: ')
segundo_val = input('Digite o segundo valor: ')

if primeiro_val > segundo_val:
    print('O primeiro valor é maior que o segundo')
elif primeiro_val >= segundo_val:
    print('O primeiro valor é maior igual que o segundo')
if primeiro_val < segundo_val:
    print('O primeiro valor é menor que o segundo')
elif primeiro_val <= segundo_val:
    print('O primeiro valor é menor igual que o segundo')
if primeiro_val == segundo_val:
    print('O primeiro valor e o segundo são iguais')
elif primeiro_val != segundo_val:
    print('O primeiro valor e o segundo são diferentes')
else:
    print('Entrou no else')            
    

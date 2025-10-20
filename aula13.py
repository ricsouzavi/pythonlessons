nome = 'Ricardo'
altura = float(1.84)
peso = 74.5

imc = (peso / altura ** 2) 

texto = f'{nome} tem {altura:.1f} e seu imc é: {imc:.5f}'   #:.3f é a quantidade de numeros nas casas decimais  #f strings serve para colocar variaveis
# print(nome, ' tem ', altura, 'de altura', 'e seu imc é: ', imc)
print(texto)
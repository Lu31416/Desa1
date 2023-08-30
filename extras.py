'''
moeda={
    'dolar_americano' : 4.91,
    'peso_argentino' : 0.02,
    'dolar_australiano' :3.18,
}

dinheiro = float(input('informe quanto dinheiro voce tem na sua carteira '))

for chave in moeda.keys():
    print(chave)
seleccion = (input('informe a qual moeda quer convertir '))

if seleccion in moeda:
    valor_convertido = dinheiro / moeda[seleccion]
    print(f"Você terá aproximadamente {valor_convertido:.2f} {seleccion}")
else:
    print("Moeda não encontrada na lista.")   

'''
'''
salario = int(input('ingrese su salario'))

if salario <= 1000:
    novosalario = salario*1.2
elif 1000 < salario < 2800:
    novosalario = salario*1.1
else:
    novosalario = salario*1.05

print(f'seu novo salario sera {novosalario}')
'''
'''
def leiaInt(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. ")

n = leiaInt('Digite um número')
print('Você digitou:', n)

'''






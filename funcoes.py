'''
def soma(x,y,z):
    w=x+y+z
    print(f'a soma e {w}')

soma(1,5,4025)

'''
'''
def soma(): 
    num1 = int(input('digite su numero'))
    calculo = 10+2+num1
    print(f'o resultado da soma e {calculo}')

soma() 
''' 
'''
def reverso_numero(numero):
    return int(str(numero)[::-1])

numero_informado = int(input("Digite um número inteiro: "))
reverso = reverso_numero(numero_informado)
print(f"O reverso do número {numero_informado} é {reverso}")

'''
'''
numero = input("Digite um número inteiro: ")
reverso = numero[::-1]
print("O reverso do número é:", reverso)
'''
'''
def c_p_f(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def f_p_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def menu():
    print("Escolha uma opção:")
    print("1. Converter de Celsius para Fahrenheit")
    print("2. Converter de Fahrenheit para Celsius")
    opcao = int(input("slecione uma opcao "))

    if opcao == 1:
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = c_p_f(celsius)
        print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}")
    elif opcao == 2:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = f_p_c(fahrenheit)
        print(f"A temperatura em Celsius é: {celsius:.2f}")
    else:
        print("intente de nuevo")

menu()
'''

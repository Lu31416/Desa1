
'''
def soma(a,b): 
    try:
        calculo = a/b
        print(f'o resultado da soma e {calculo}')
    except ZeroDivisionError:
        print('no e posivel')
    except TypeError as e:
        print(f'no podee')



soma(10,'m') 

'''
file = 'arquivo.txt'

    #escrita
arquivo_escrito = open(file, "w") #open soamente para leitura
arquivo_escrito.write("texto a ser escritoooooooooooo")
'''
'''
'''
try:
    # Seu código que pode gerar exceções
    valor = int(input("Digite um número: "))
    resultado = 10 / valor
except (ValueError, TypeError):
    print("Ocorreu um erro de tipo ou valor.")
'''
def minha_funcao(*args):
    print("Outros argumentos:", args)

minha_funcao()  # Chamada com apenas um argumento
  # Chamada com vários argumentos

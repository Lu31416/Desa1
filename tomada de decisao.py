'''
num1=int(input('ingrese un numero'))
num2=int(input('ingrese otro numero') )

if num1>=num2:
    print(f'o maior numero e {num1}')
else:
    print(f'o maior numero e {num2}')
'''
'''
turno = input('ingrese el turno M-matutino ou V-Vespertino ou N- Noturno ')

if turno=="M":
    print('bom dia')
elif turno =="V":
    print('boa tarde')
elif turno =="N":
    print('boa noite')
else:
    print('valor invalido!')
'''

while True:
    nota = int(input(f'ingrese una nota entre zero e dez '))
    if nota >=0 and nota <=10:
        print('muy biennn')
        break
    else:
        print('reintente')

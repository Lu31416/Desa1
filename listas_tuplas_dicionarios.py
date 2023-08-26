'''
medias = []
for aluno in range(10):
    print(f'notas do aluno{aluno+1}:')
    notas=[]
    for i in range(2):
        nota = float(input(f'digite a nota{i + 1}:'))
        notas.append(nota)

    media = sum(notas) / len(notas)
    medias.append(media)

print(medias)

alunos_aprovados = sum(1 for media in medias if media >= 7.0)

print(f'Nro de alunos com média maior ou igual a 7.0: {alunos_aprovados}')
'''
'''
nome = input('ingrese su nombre')
nome_invertido = ''
for n in nome:
    nome_invertido = n + nome_invertido

print('seu nome invertido', nome_invertido)
'''
'''
valores = {
    'pedro': 5,
    'maria': '',
    'peras': 1,
}

for chave, valor in valores.items():
    if not valor:
        print('a lista tem valores faltantes')
        break
    else:
        print('los valores son:', chave, valor)
'''
'''
perguntas ={
    'Telefonou para a vítima?' : '',
    'Esteve no local do crime?': '',
    'Mora perto da vítima?' : '',
    'Devia para a vítima?': '',
    'Já trabalhou com a vítima?' : '',
}

respostas_positivas = 0
for x,y in perguntas.items(): 
    resposta = input(f'Responda"{x}"sim/nao:')
    if resposta =='sim':
        respostas_positivas += 1

if respostas_positivas == 5:
    print('assassino')
elif 3 <= respostas_positivas < 4:
    print('cumplice')
elif 2 <= respostas_positivas < 3:
    print('suspeita')
else:
    print('inocente')
'''

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




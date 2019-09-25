resposta = ''
lista = []
aux = 0
while resposta != 'nao':
    resposta = input("Quer adicionar um novo valor?(Sim|Não)")
    if resposta == 'sim':
        aux = input("Digite o novo valor:")
        lista.append(aux)
        print(f"Lista é: {lista}")
        print(type(lista))
    else:
        print(f"Finalizando a lista com o valor de: {lista} e tipo: {type(lista)}")



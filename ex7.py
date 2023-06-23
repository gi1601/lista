lista = []
while True:
    num = int(input("Adicione um número: "))
    for i in lista:
        if num in lista:
            lista.remove(i)
    lista.append(num)
    sair = str(input("Quer sair?"))
    if sair == "s":
        break
lista.sort()
print(lista)


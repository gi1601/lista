lista = []
while True:
    num = int(input("Adicione um número: "))
    if num in lista:
        lista.pop()
    lista.append(num)
    sair = str(input("Quer sair?"))
    if sair == "s":
        break
lista.sort()
print(lista)


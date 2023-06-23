lista =[]
mult = 1

while True:
    numero = int(input("Informe o núemro ou 0 para parar: "))
    lista.append(numero)
    if numero == 0:
        lista.remove(0)
        break

qtd = len(lista)
lista.sort(reverse = True)
print(f'A quantidade é: {qtd}')
print(f'Ordem decrescente: ',lista)
if 5 in lista:
    print("Já possui o número 5 na lista")
else:
    print("Não possui o número 5 na lista")
lista= []

while True:
    numero=(int(input("Digite um número ou zero para parar: ")))
    lista.append(numero)
    if numero== 0:
        lista.remove(0)
        break


menor = min(lista)
soma = sum(lista)


print(f"Soma:{soma}")
print(f"Menor:{menor}")

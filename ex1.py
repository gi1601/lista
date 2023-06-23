lista= []
mult=1

while True:
    numero=(int(input("Digite um número ou zero para parar: ")))
    lista.append(numero)
    if numero== 0:
        lista.remove(0)
        break


maior = max(lista)
menor = min(lista)
soma = sum(lista)
for i in lista:
    mult*= i


print(lista)
print(f"Soma:{soma}")
print(f"Maior:{maior}")
print(f"Menor:{menor}")
print(f"Multiplicação:{mult}")

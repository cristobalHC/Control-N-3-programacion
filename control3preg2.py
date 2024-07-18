def convierte_negativo(lista):
    valor_negativo=-valor
    lista.remove(valor)
    lista.append(valor_negativo)
    return valor

lista=[]
for x in range(10):
    valor = float(input("ingrese los numeros:"))
    lista.append(valor)
convierte_negativo(lista)
print(lista)
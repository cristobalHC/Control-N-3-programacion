def solo_numeros(var):
    if var!=str:
        return False
    if var!=float:
        return True

var=str(input("ingrese una palabra o valor:"))
print(solo_numeros(var))
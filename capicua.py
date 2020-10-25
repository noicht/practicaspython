num = int(input("Ingrese un numero:"))
aux = num
reversa = 0
while(num>0):
    digito = num%10
    reversa = reversa*10 + digito
    num = num//10
if(aux == reversa):
    print("ES CAPICUA")
else:
    print("NO ES CAPICUA")

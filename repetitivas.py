n=int(input("\nDigite el valor de los primeros numeros que desea sumar: "))

i=1
sum=0

while i<=n:
    sum= sum + i
    i = i + 1

print("\nLa suma de los primeros " + str(n) + " numeros es: " + str(sum))
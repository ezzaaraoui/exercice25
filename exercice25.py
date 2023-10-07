nombre=int(input("Donner un nombre SVP : "))



while nombre<=0 :
    nombre=int(input("Donner un nombre SVP (positif non null): "))

factorielle=1

for i in range(1,nombre+1):
    factorielle = factorielle * i

print("la factorielle de ",nombre," est : ",nombre,"! = ",factorielle)
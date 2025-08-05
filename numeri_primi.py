import math
numero=int(input("inserisci un numero intero maggiore di 3: "))
print("\nEcco tutti i numeri primi fino a", numero)
#stampo i primi due numeri primi
print("2 3", end=' ')

#itero su tutti i numeri dispari n che voglio esaminare
for n in range(3, numero+1, 2):
    i=3
    
    #itero su tutti i possibili divisori del numero n in esame
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n%i==0:
            break   #interrompe il ciclo se n ha un divisore esatto
        #verifico se n è primo e lo stampo
        # NB: i è certamente definito, perché inizializzato
    if n%i !=0:
        print(n, end=' ')


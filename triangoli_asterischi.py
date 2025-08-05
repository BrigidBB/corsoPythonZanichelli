righe=int(input("\nInserisci il numero (intero) delle riche: "))
#il primo ciclo ha la funzione di contatore delle righe
for i in range(righe):
    #a ogni riga si va a capo e si rientra, come parte del ciclo esterno
    print(' ')
    print("\t", end=' ' )
    #il ciclo annidato riempie ogni riga con un numero crescente di asterischi
    for j in range(i+1):
        print("*", end=' ')
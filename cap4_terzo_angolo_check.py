
alfa=int(input("Inserisci il valore intero di un angolo in gradi e che sia minore di 90°: "))
beta=int(input("Inserisci il valore intero di un angolo in gradi e che sia minore di 45°: "))
if alfa<=0 or beta<=0 or alfa+beta>=180: print("errore, controlla i dati di input inseriti")
else:
    gamma=180-alfa-beta
    print("gamma vale", gamma," gradi")  
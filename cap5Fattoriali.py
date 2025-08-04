numero=int(input("inserisci un numero positivo o nullo, minore di 21, e premi invio: "))
#DEVO INIZIALIZZARE!!!!!!!!!!!! IMP.SSIMO
fattoriale=1
if numero>=0 and numero<21:
    for i in range(1,numero+1,1):
        fattoriale*=i
    print("il fattoriale di", numero, "è", "{:,}".format(fattoriale).replace(',', '\''))
else:
    print("numero di input non valito, cazzone!")
numero1=float(input("Inserisci il primo numero decimale: "))
numero2=float(input("Inserisci il secondo numero decimale: "))
if numero1>numero2:
    differenza=numero1-numero2
    print("il numero maggiore è: ", format(numero1,".2f"),"\n","e supera l'altro numero di ",format(differenza,".2f"))
elif numero1<numero2:
    differenza2=numero2-numero1
    print("il numero maggiore è: ", format(numero2,".2f"),"\n","e supera l'altro numero di ",format(differenza2,".2f"))
else:
    print("i due nunmeri inseriti sono uguali")
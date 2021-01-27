#Organizza con un dizionario i dati sui conti correnti bancari con un numero del conto e saldo.
#Fornito poi il numero del conto, il programma visualizza il saldo oppure un messaggio nel caso in cui il conto non sia presente nella mappa.

n_conto = ["IT 76 A 98564 98564 146578920361", "IT 65 A 78694 78694 561081985746", "IT 14 A 35678 35678 198745620953"]
saldo = ["60000 €", "5000 €", "800000 €"]
dictionary = {}
for n in range(len(n_conto)):
    dictionary[n_conto[n]] = saldo[n]
n_conto_input = input("Inserire il conto per conoscere il saldo di esso: ")
if n_conto_input in n_conto:
    print("Saldo :", dictionary[n_conto_input])
else:
    print("Il conto inserito non è presente nel database. Riprovare")
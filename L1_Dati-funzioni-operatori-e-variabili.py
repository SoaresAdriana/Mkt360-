# 1. ISTRUZIONI, DATI E OPERATORI

# 1.1 Usare print() con testi e numeri

from tkinter import CASCADE


print('Ciao Mondo!')

print('Ciao Mondo!',"Ciao Universo!")
# La virgila, infdatti, permete di "concatenare"due testi e i caratteri delle virgolette alte e degli apice possono coesistere, purché "aperti" e "chiusi" corretamente usano lo stesso carattere per includere la porzione di testo, anche nella stessa istrizione. Lo stesso risultato si può ottenere usando il segno di assizione per esempio:
print('Ciao Mondo!'+"Ciao Universo!")
# Potete utilizzare questo tipo di "adizione"anche in modo diretto, come con le operazione con i numeri as esempio:
"Ciao"+"Mondo"

# 1.1.1 Numeri
print(136-5+1)
print(15+10*3)
print("x"*2)
print("x"*10)

# 2. STRINGHE, NUMERI E TIPI DI DATI 
x = 'casa'
type(x)
x = 42
# Un valore di testo, in informatica, viene detto "stringa", a indicare una sequenza di caratteri (lettere, numeri, punteggiatura e altri segni) che ha un valore letterale in quanto "testo". Ciò vuoi dire che la stringa "42" non sarà mai trattata como il valore corrispondente e che la stringa "15-3" non darà mai un risultato, in quanto viene interpretata, appunto, come semplice sequenza di quattro caratteri 1,5, - e 3. Nel caso provassimo a utulizzare il conttenuto di una stringa con funzioni dedicate ai numeri, questa distribuizione produrrebbe quindi un errore. Questa funzione si chiama type() permette di indentificare il tipodi valore specificato.

# 3. NUMERI INTERI E SISTEMI NUMERICI
print(1234123412341234123412341234123412341234+1)
bin(128)
int(3.14)
round(3.14159,3)
float(36)
[1,2,8,36,48,52]
["ciao","mondo","mondo","buongiorno","universo","come","va"]
set([1,2,3,4,5,1,2,3,4,5,6])
età=45
print(età*2)




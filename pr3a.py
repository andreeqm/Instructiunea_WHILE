"""Se citesc numere de la tastatură până la introducerea unui număr impar divizibil cu 3. 
Să se afişeze suma tuturor numerelor pare introduse. 
 Exemplu: Date de intrare  7  4   6   2   1   9   Date de ieşire 12."""

n=eval(input('Introduceti un numar:'))
s=0

while n%2==0 or (n%2!=0 and n%3!=0):
    if n%2==0:
        s+=n
    
    n=eval(input('Introduceti un numar:'))

print('Suma numerelor pare introduse:',s)

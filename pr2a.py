"""Se citesc pe rând temperaturile medii ale fiecărei luni a unui an, ca numere întregi. 
Să se afişeze cu două zecimale media anuală a temperaturilor pozitive şi a celor negative. 
Exemplu: Date de intrare  -5  -3  1  8  12  17  20  21  18  10  6  -2  Date de ieşire  medie_poz=13.66  medie_neg=-3.33."""

n=0
sp=0
sn=0
np=0
nn=0
c=0

while c<12:
    n=eval(input('Introduceti temperatura:'))
    if n<55 and n>-60:
        c+=1
        if n>0:
            sp+=n
            np+=1
        elif n<0:
            sn+=n
            nn+=1 
    else: print('Error: Introduceti o temperatura valida')           

if np>0:
    print('medie_poz=',round(float(sp/np), 2))
else:print('Nu au fost temperaturi pozitive')

if nn>0:
    print("medie_neg=",round(float(sn/nn), 2))
else:print("Nu au fost temperaturi negative")
"""Se introduc succesiv numere nenule până la introducerea numărului 0. 
Să se afişeze suma tuturor numerelor introduse. 
Exemplu: Date de intrare   3  5  4  2  0  Date de ieşire 14."""

nr=1
suma=1
while((nr>0)and(nr!=0)):
    suma+=nr
    nr=eval(input("Introduceti numerele: "))

print("suma numerelor este",suma)

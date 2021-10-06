x = input('entrez les heures:')
y = input('entrez le taux:')
try:
    heure = float(x)
    taux = float(y)
except:
    print('Error,Please enter the numeric digit:')
    exit()
if heure<=40:
    print(heure*taux)
else:
    print((((heure-40)*taux)*1.5)+taux*40)
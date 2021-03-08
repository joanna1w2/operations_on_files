# -*- coding: utf-8 -*-
#===================================================================
# 	IMPORTS 
#===================================================================

# no imports

#===================================================================
# 	FUNKCJA
#===================================================================
	
	
	
"""
Wczytuje plik z zawartoscia czesci genomu bakterii
'Acetobacter pasterianus' jako string i oblicza czestosc wystepowania A , C , G , T.
	in  : 
		ls - zawartosc pliku
		litera - litera dla ktorej chcemy obliczyc czestosc wystepowania
	out :
		licznik_liter
"""
def ilosc_liter(ls,litera):
	
	licznik_liter = 0
	L = len(ls)
	
	for i in range(0,L):
		element = ls[i]
		if element == litera :
			licznik_liter = licznik_liter + 1
	
	return licznik_liter
	


#===================================================================
# 	PROGRAM GLOWNY
#===================================================================
print '=============================================================='

#A = Adeniny
#C = Cytozyny
#G = Guaniny
#T = Tyminy

#-------------------------------------------
# wczytywanie pliku :

file_name = "Acetobacter_pasterianus.txt"

f = open(file_name,'rb')

st = f.read()

f.close()

print "st = " , st


#-------------------------------------------
# liczenie czestosci dla litery 'A' :

letter = 'A'

ilosc_liter_A = ilosc_liter(st,letter)
print "ilosc liter = " , ilosc_liter_A

L = len(st)
print "L = " , L

czestosc_A = ilosc_liter_A/float(L) 
print "czestosc_A = " , czestosc_A    

#-------------------------------------------
# liczenie czestosci dla litery 'C' :

letter = 'C'

ilosc_liter_C = ilosc_liter(st,letter)
print "ilosc liter = " , ilosc_liter_C

czestosc_C = ilosc_liter_C/float(L) 
print "czestosc_C = " , czestosc_C    




#-------------------------------------------
# liczenie czestosci dla litery 'G' :

letter = 'G'

ilosc_liter_G = ilosc_liter(st,letter)
print "ilosc liter = " , ilosc_liter_G

czestosc_G = ilosc_liter_G/float(L) 
print "czestosc_G = " , czestosc_G    


#-------------------------------------------
# liczenie czestosci dla litery 'T' :

letter = 'T'

ilosc_liter_T = ilosc_liter(st,letter)
print "ilosc liter = " , ilosc_liter_T

czestosc_T = ilosc_liter_T/float(L) 
print "czestosc_T = " , czestosc_T    




#float sluzy zeby liczbe int(calkowita) na float(zmiennoprzcinkowa)
#co robi float w programie?
#zamienia st zeby byla liczba i mozna bylo ja policzyc



# program napisany = 04/11/2016
#===================================================================
# 	END OF FILE
#===================================================================
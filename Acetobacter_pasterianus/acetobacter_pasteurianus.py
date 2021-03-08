# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

"""
Reads the content of the file which contains part of the genome information of the
Acetobacter Pasteuranius and calculates the amount of occurences of A, C, G, T.
	in  : 
		ls - the content of the file
		letter - the letter for which we want to calculate the amount of occurences
	out :
		letter_counter
"""

def letter_counter(ls,letter):
	
	letter_counter = 0
	L = len(ls)
	
	for i in range(0,L):
		element = ls[i]
		if element == letter :
			letter_counter = letter_counter + 1
	
	return letter_counter


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('============================================================= \n')

# A = Adenine
# C = Cytosine
# G = Guanine
# T = Thymine

#-------------------------------------------
# reading the content of the file :

file_name = "Acetobacter_pasterianus.txt"
f = open(file_name,'rb')
st = f.read()
f.close()

# print(" st = " , st)

#-------------------------------------------
# counting the amount of each letter :


ls_letters = ['A', 'C', 'G', 'T']
L = len(ls_letters)

Lst = len(st)
print(" Total amount of letters :" , Lst , "\n")

for i in range(0,L):
	letter = ls[i]
	
	# counting the amount of occurences:
	amount_of_occurences = letter_counter(st, letter)
	print(" Amount of occurencies of :" , letter, "=" , amount_of_occurences)
	
	# counting the frequency :
	letter_freq = amount_of_occurences / float(Lst)
	print(" Frequency :" , letter_freq , "\n")
   


# date : 04/11/2016
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

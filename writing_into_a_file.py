# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# quick program demonstrating how to write into a txt file;


# name the file;
file_name = "my_first_file.txt"

f = open( file_name, 'wb' ) 		# open the file;
										# note : if the file does not exist it will be created automatically;

# to write into the txt file, use the .write function

f.write("Writing information into a file : \n\n\n")

f.write("After every inputted string, you must go onto the next line, \n")
f.write("you do that using the special symbol \\n at the end of the string. \n")

"""
notes :
	
	writing into a txt file is much faster (~100 - 1000 times) than printing messages
	on the screen.
	
	doing this is called "logging" (pl: logowanie). this way, the information on the output
	is much clearer.
"""


f.close()			# close the file; this should always be the last line of code after writing into a file
						# if you write any code related to the file after this, it will not be recognised

print("\n\n")
print("Inputting data completed.")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

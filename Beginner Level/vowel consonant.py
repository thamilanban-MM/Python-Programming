r=raw_input("")
list=['a','e','i,'o','u']
if r.isdigit():
	print("Invalid input")
else:
	if r in list:
		print("Vowel")
	else:
		print("Consonant")

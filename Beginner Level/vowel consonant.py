r=raw_input("")
list=['a','e','e','o','u']
if r.isdigit():
	print("enter the valid input")
else:
	if r in list:
		print("Vowels")
	else:
		print("Consonant")

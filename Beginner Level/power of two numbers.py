a=raw_input()
b=raw_input()
if a.isdigit():
	a=int(a)
	b=int(b)
	pwr=a**b
	print pwr
else:
	print ("invalid input")

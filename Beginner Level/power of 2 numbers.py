a,b=raw_input().split()
if a.isdigit():
	a=int(a)
	b=int(b)
	pwr=a**b
	print pwr
else:
	print ("invalid input")

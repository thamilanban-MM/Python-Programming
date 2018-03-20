a=raw_input("")
b=raw_input("")
c=raw_input("")
if isinstance(a,str) and isinstance(b,str) and isinstance(c,str):
	if (((a>='a') and (a<='z')) or((a>='A') and (a<='Z')) and ((b>='a') and (b<='z')) or ((b>='A') and (b<='Z')) and ((c>='a')  and (c<='z')) or ((c>='A') and (c<='Z'))):
		print("invalid input")
	else:
		a=int(a)
		b=int(b)
		c=int(c)
		if (a>b) and (a>c):
			print a
		elif (b>a) and (b>c):
			print b
		else:
			print c

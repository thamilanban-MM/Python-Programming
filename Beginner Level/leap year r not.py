r=raw_input("")
if isinstance(r,str):
	if ((r>='a') and (r<='z')):
		print("invalid input")
	else:
		r=int(r)
		if (r%4==0 and (r%100!=0 or r%400==0)):
			print("yes")
		else:
			print("no")
			

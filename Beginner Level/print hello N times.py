N=raw_input("")
if isinstance(N,str):
	if ((N>='a') and (N<='z') or (N>='a') and (N<='z')):
		print("invalid input")
	else:
		for i in range (1,int(N)+1):
			print("Hello")

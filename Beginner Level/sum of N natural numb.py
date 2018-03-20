N=raw_input("")
if isinstance(N,str):
	if ((N>='a') and (N<='z') or (N>='A') and (N<='Z')):
		print("invalid input")
	else:
		N=int(N)
		sum=(N*(N+1))/2
		print(sum)

k=raw_input()
if k.isdigit():
	k=int (k)
	temp=k
	rev=0
	while(k>0):
		dig=k%10
		rev=rev*10+dig
		k=k//10
	if(temp==rev):
		print ("yes")
	else:
		print ("no")
else:
	print ("invalid")

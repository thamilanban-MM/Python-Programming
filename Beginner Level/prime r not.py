k=raw_input()
if k.isdigit():
	k=int (k)
	if (k >= 1):
		for i in range (2,k):
			if(k%i==0):
				print ("no")
				break
		else:
			print("yes")
	else:
		print ("no")
else:
	print ("invalid")

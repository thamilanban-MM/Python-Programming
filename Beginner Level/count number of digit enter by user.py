a=(raw_input())
sum=0
if a.isdigit():
	a=int(a)
	while (a>0):
		r=a%10
		sum=sum+1
		a=a/10
	print sum
else:
	print ("invalid input")

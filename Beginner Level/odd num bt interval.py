x, y = raw_input().split()
if x.isdigit() and y.isdigit():
	x=int(x)
	y=int(y)
	for i in range (x+1,y):
		if(i%2!=0):
		       print(i)
else:
	print("invalid")

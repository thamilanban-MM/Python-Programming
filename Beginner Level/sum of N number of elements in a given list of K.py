n=raw_input()
k=raw_input()
if n.isdigit() and k.isdigit():
	n=int(n)
	k=int(k)
	p=[]
	sum=0
	for i in range (1,n+1):
		r=raw_input()
		if r.isdigit():
			p.append(r)
			for j in range (0,k):
				sum=sum+p[j]
			print sum
		else:
			print "invalid"
else:
	print "invalid"

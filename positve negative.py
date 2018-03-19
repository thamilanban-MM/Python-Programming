a=raw_input("")
if a.isdigit():
	if (int(a)>0):
		print("Positive")
	elif (int(a)<0):
		print("Negative")
	else:
		print("Zero")
else:
	print("enter the invalid number")

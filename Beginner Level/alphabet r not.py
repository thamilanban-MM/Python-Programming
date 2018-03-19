ch = raw_input("")
if ch.isdigit():
	print("No")
else:
    if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    	print("Alphabet")
    else:
    	print("invalid input")

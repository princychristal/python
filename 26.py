try:
	n=input()
	(a,b)=(0,0)
	for i in n:
		if i.isnumeric():
			a=a+1
		else:
			b=b+1
	print("number of words :"+str(b))
	print('number of integers:'+str(a))
except:
	print('invalid')

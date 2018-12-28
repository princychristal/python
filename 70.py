try:
	a=int(input())
	for x in range(a):
		b=2**x
		if b>a:
			print(b);
			break
except:
	print('invalid');

def near():
	a=int(input())
	while(True):
		if a%10==0:
			break
		a=a+1
	print(a);
try:
	near()
except:
	print('invalid');

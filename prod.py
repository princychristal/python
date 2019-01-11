def proddig():
	a=int(input())
	b=1
	while(a!=0):
		r=a%10
		b=b*r
		n//=10
	print(b);
try:
	proddig()
except:
	print('invalid');

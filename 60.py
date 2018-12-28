def fibo(a):
	if a==1 or a==0:
		return(a)
	else :
		return fibo(a-1)+fibo(a-2)
try:
	a=int(input())
	sum=0
	for x in range(0,a):
		print(fibo(x));
except:
print('invalid');

def fib(a):
	if a==1 or a==0:
		return(a)
	else :
		return fib(a-1)+fib(a-2)
try:
	a=int(input('Enter a :'))
	sum=0
	for i in range(0,a):
		print(fib(i));
except:
print('invalid');

def lcm():
	(a,b)=map(int,sys.stdin.readline().split())
	temp=min(a,b)
	while(True):
		if temp%a==0 and temp%b==0:
			break
		temp+=1
	print(temp);
try:
	lcm()
except:
	print('invalid');

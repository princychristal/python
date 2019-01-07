 def main():
	x=[]
	while(True):
		s=input()
		try:
			if '/' in s:
				a,b = map(int,s.split('/'))
				c=a/b
			else :
				a,b=map(int,s.split('%'))
				c=a%b
			x.append(int(c))
			c=[]
		except ValueError:
			break
	for i in x:
		print(i);
try:
	main()
except:
	print('invalid');

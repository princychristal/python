def countsen():
	s=input()
	print(s);
	a=1
	for x in range(len(s)):
		if s[x]==' ':
			a+=1
	print(a);
try:
	countsen()
except:
	print('invalid') ;

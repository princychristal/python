def pal():
	s1=input()
	s2=s1[::-1]
	if s1==s2:
		print('yes');
	else :
		print('no');
try:
	pal()
except:
	print('invalid');

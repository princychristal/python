def checkbin():
	a=['0','1']
	b=0
	s=input()
	for x in range(len(s)):
		if s[x] in a:
			continue
		else :
			b=1
			break
	if b!=1:
		print('yes');
	else :
		print('no');

def compo():
	a=int(input())
	b=0
	for x in range(2,a//2):
		if a%x==0:
			b=1
			break
	if b==1:
		print('yes');
	else :
		print('no');
try:
	compo()
else :
	print('invalid');

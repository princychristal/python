def compare(s1,s2):
	if s1==s2:
		print(s2);
	elif s1>s2:
		print(s1);
	else :
		print(s2);
def main():
	try:
		a=input()
		b=input()
		compare(a,b)
	except:
		print('invalid');
main()

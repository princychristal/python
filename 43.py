def compare(s1,s2):
	for i in range(len(s2)):
		s1+=s2[i]
	print(s1);
def main():
	try:
		a=input()
		b=input()
		compare(a,b)
	except:
		print('nvalid');
main()

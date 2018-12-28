def checkrange(i):
	if i in range(1,11):
		print('yes');
	else :
		print('no');
def main():
	try:
		i=int(input())
		checkrange(i)
	except:
		print('invalid');
		
main()

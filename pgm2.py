x=(input("N="))
if(x.isalpha()==False):
    n=int(x)
    if(n%2!=0):
        print("odd")
    elif(n%2==0):
        print("even")
    else:
        print("zero")
else:
    print("the input is invalid")

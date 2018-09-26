y=int(input("y="))
z=int(input("z="))
for x in range(y+1,z):
    if(x%2==0):
        print(x)
else:
    print("input is invalid")

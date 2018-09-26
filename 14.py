y=int(input("y="))
z=int(input("z="))
if(y<=100000)&(z<=10000):
    for x in range(y,z+1):
     if(x%2!=0):
        print(x)
else:
      print("input is invalid")

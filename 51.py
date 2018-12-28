try:
        x=int(input())
        si=''
        while(n!=0):
                si+=sr(x%10)
                x//=10
        for y in range(len(si)-1,-1,-1):
                print(si[y])
except:
        print('invalid');

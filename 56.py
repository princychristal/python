def main():
        try:
                a=0
                b=0
                n=input()
                for x in n:
                        if x.isalpha():
                                a=a+1
                        elif x.isnumeric():
                                b=b+1
                if a+b==len(n) and a>0 and b>0:
                        print('yes');
                else :
                        print('no');
        except:
                print('invalid');
main()

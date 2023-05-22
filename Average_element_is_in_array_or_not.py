n=int(input())
l=list(map(int,input().split()))
c=sum(l)//len(l)
if c in l:
    print("True")
else:
    print("False")
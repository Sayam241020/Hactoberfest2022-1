a=int(input())
b=int(input())
c=int(input())
if a>=b and b>=c:
    print(a)
elif b>=c:
    print(b)
else:
    print(c)
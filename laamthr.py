a,b,c=input("").split()
a=int(a)
b=int(b)
c=int(c)
if(a>b and a>c):
	print(a,end="")
elif(b>c and b>a):
	print(b,end="")
else:
	print(c,end="")

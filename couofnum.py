n=int(input(""))
count=0
for i in range(1,n+1):
	while(n>0):
		count+=1
		n=n//10
print(count,end="")

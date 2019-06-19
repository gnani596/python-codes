def isprime(a):
	for i in range(2,int(a/2)+1):
		if(a%i==0):
			return 0
			break
	else:
		return 1
n=int(input())
sum=2
c=0
for i in range(3,n):
	if sum<=n:
		if isprime(i):
			sum=sum+i
			if isprime(sum) and sum<=n:
				print(sum)
				c=c+1
	if sum>n:
		break
print(c)
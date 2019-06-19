import math
a,b = map(int,input().split())
count = 1
if a>b:
	for i in range(2,(int)(math.sqrt(b))+1):
		if(b%i == 0):
			j = b/i
			if(a%i == 0 or a%j == 0):
				count+=1
			if(j==i):
				count -=1
else:
	for i in range(2,(int)(math.sqrt(a))+1):
		if(a%i == 0):
			j = a/i
			if(b%i == 0 or b%j == 0):
				count+=1
			if(j==i):
				count -=1
print(count)
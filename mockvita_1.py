def fact(n):
	if(n==0 or n==1):
		return 1
	else:
		return fact(n-1)*n

alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 																																																																																																																																				

x = int(input())
s = int(input())
y = int(input())
m = int(input())
z = int(input())
c = int(input())
Q1 = list(map(str,input().split()))
Q2 = input()

simple = alphabets[:x]
medium = alphabets[x:x+y]
complexx = alphabets[x+y:x+y+z]

no_of_ways = int((fact(x)/(fact(s)*(fact(x-s)))) * (fact(y)/(fact(m)*(fact(y-m)))) * (fact(z)/(fact(c)*(fact(z-c)))) )
print(no_of_ways)

count = 1
if Q2 in simple:
	simple.remove(Q2)
	x = x-1
elif(Q2 in medium):
	medium.remove(Q2)
	y = y-1
elif(Q2 in complexx):
	complexx.remove(Q2)
	z = z-1


for i in Q1:
	if i in simple and x-1>=s:
		count+= int((fact(x-1)/(fact(s)*(fact(x-s-1)))) * (fact(y)/(fact(m)*(fact(y-m)))) * (fact(z)/(fact(c)*(fact(z-c)))) )
	elif i in medium and y-1>=m:
		count+= int((fact(x)/(fact(s)*(fact(x-s)))) * (fact(y-1)/(fact(m)*(fact(y-m-1)))) * (fact(z)/(fact(c)*(fact(z-c)))) )
	elif i in complexx and z-1>=c:
		count+= int((fact(x)/(fact(s)*(fact(x-s)))) * (fact(y)/(fact(m)*(fact(y-m)))) * (fact(z-1)/(fact(c)*(fact(z-c-1)))) )

print(count)


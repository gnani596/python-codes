array = list(map(int,input().split(',')))
M1,M2 = 0,0
flag_M = 0
for i in array:
  if(i<=1 and i>M1):
    M1 = i
    flag_M = 1
if M1 in array:
    array.remove(M1)
for i in array:
  if(M1 == 0 and i>M2):
    M2 = i
  elif(M1==1 and i<=2 and i>M2):
    M2 = i
if M2 in array:
    array.remove(M2)    
month = str(M1)+str(M2)


D1,D2 = 0,0
for i in array:
  if(month == '02' and i<=2 and i>D1):
    D1 = i
  elif(month != '02' and i<=3 and i>D1):
    D1 = i
if D1 in array:
    array.remove(D1)
for i in array:
  if(month == '02' and D1<=1 and i>D2):
    D2 = i
  elif(month == '02' and D1==2 and i<=8 and i>D2):
    D2 = i
  elif(month in ('04','06','09','11') and D1<=2 and i>D2):
    D2 = i
  elif(month in ('04','06','09','11') and D1==3):
    D2 = 0
  elif(month in ('01','03','05','07','08','10','12') and D1<= 2 and i>D2):
    D2 = i
  elif(month in ('01','03','05','07','08','10','12') and D1==3 and i<=1 and i>D2):
    D2 = i
if D2 in array:
    array.remove(D2)
day = str(D1)+str(D2)

h1,h2 = 0,0
for i in array:
  if(i<=2 and i>h1):
    h1 = i
if h1 in array:
    array.remove(h1)
for i in array:
  if(h1<=1 and i>h2):
    h2 = i
  elif(h1==2 and i<=3 and i>h2):
    h2 = i
if h2 in array:
    array.remove(h2)
hour = str(h1)+str(h2)


m1,m2 = 0,0
for i in array:
  if(i<=5 and i>m1):
    m1 = i
if m1 in array:
    array.remove(m1)
for i in array:
  if(i>m2):
    m2 = i
if m1 in array:
    array.remove(m1)
minutes = str(m1)+str(m2)

if(flag_M == 0):
  print(0)
else:
  print(month+'/'+day+' '+hour+':'+minutes)
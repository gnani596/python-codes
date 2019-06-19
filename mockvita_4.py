from itertools import permutations as p
for _ in  range(int(input())):
    n = int(input())
    array = [1]
    bad_perm = []
    for i in range(2,n+1):
        if(n%i==0):
            array.append(i)
    perm  =list(p(array))
    perm.remove(tuple(array))
    count = len(perm)
    for i in perm:
        for j in range(len(array)-1):
            for k in range(len(array)-1):
                if(tuple(array[j:j+2]) == i[k:k+2]):
                    if i not in bad_perm:
                        bad_perm.append(i)
    print(count-len(bad_perm))
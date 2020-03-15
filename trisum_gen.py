#input: num
#output: all triple that aa+bb=cc, a<b<c
#3,4,5
#6,8,10
#in 1,2,3,4,5,6,7,8,9,10
import sys
num=int(sys.argv[1])

for i in range(1,num+1):
    for j in range(1,i):
        ssum=i+j
        if ssum <=num:
            print('trisum(',j,',',i,',',ssum,').')
        else:
            break


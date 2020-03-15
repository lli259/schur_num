import os
import time

def getruntime(numb):
    s=time.time()
    os.system('python trisum_gen.py '+str(numb)+' > trisum/trisum'+str(numb)+'.lp')
    e=time.time()
    return round(e-s,3)

with open('time_python_gen.csv','w') as f:
    f.write('n,pythontime\n')
for i in range(8,1000,30):
    with open ('time_python_gen.csv','a') as f:
        t=getruntime(i)
        f.write(str(i)+','+str(t)+'\n')



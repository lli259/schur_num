import os
import time

def getruntime(numb):
    s=time.time()
    os.system('gringo enc_schur_trisum.lp trisum/trisum'+str(numb)+'.lp -c n='+str(numb)+"|clasp --time-limit=2000")
    e=time.time()
    return round(e-s,3)

with open('time_trisum_schur.csv','w') as f:
    f.write('n,trisumtime\n')
for i in range(8,1000,30):
    print(i)
    with open ('time_trisum_schur.csv','a') as f:
        t=getruntime(i)
        f.write(str(i)+','+str(t)+'\n')



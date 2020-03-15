import os
import time
import pandas
'''
df=pandas.read_csv('all/all.csv')
index=list(df['n'])
'''

files=sorted(os.listdir("./trisum"))

index=[int(i.split('.')[0].split('um')[1]) for i in files]
index=sorted(index)

def getruntime(numb):
    s=time.time()
    os.system('gringo enc_schur_original_xyz.lp -c n='+str(numb)+' |clasp --time-limit=2000')
    e=time.time()
    return round(e-s,3)

with open('time_original_xyz_schur.csv','w') as f:
    f.write('n,originaltime\n')
for i in index:
    with open ('time_original_xyz_schur.csv','a') as f:
        t=getruntime(i)
        f.write(str(i)+','+str(t)+'\n')



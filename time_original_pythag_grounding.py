import os
import time

files=sorted(os.listdir("./trisum"))

nums=[int(i.split('.')[0].split('um')[1]) for i in files]
nums=sorted(nums)
'''
def getruntime(numb):
    s=time.time()
    os.system('gringo enc_t_tsum.lp tsum/tsum'+str(numb)+'.lp -c n='+str(numb)+' > t.txt')
    e=time.time()
    return round(e-s,3)

with open('t_tsum_result_ground.csv','w') as f:
    f.write('n,sqsumtime\n')
for i in nums:
    print(i)
    with open ('t_tsum_result_ground.csv','a') as f:
        t=getruntime(i)
        f.write(str(i)+','+str(t)+'\n')
'''



def getruntime2(numb):
    s=time.time()
    os.system('gringo enc_t_original.lp -c n='+str(numb)+' > t.txt')
    e=time.time()
    return round(e-s,3)

with open('t_original_result_ground.csv','w') as f:
    f.write('n,originaltime\n')
for i in nums:
    if i > -1:
        print(i)
        with open ('t_original_result_ground.csv','a') as f:
            t=getruntime2(i)
            f.write(str(i)+','+str(t)+'\n')




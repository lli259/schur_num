import pandas as pd
import matplotlib.pyplot as plt
import sys

f1=pd.read_csv(sys.argv[1])
f1=f1.set_index("n")

def pltsorttime(r,c):	
	plt.plot(f1.index.values,f1[r],label=r,color=c)


pltsorttime(f1.columns.values[0],'red')

pltsorttime(f1.columns.values[1],'blue')

pltsorttime(f1.columns.values[2],'black')
pltsorttime(f1.columns.values[3],'purple')
'''
'''
plt.legend()
plt.ylabel('runtime')
plt.xlabel('n')
plt.grid()
plt.show()

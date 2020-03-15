import pandas as pd
#input enct1_result.csv:
#ins,model,time,groundsize

#combine runtime together
import os
files=sorted(os.listdir("./all"))
print(files)
allresults=[i for i in sorted(files) if ".csv" in i]
allresults=['all/'+i for i in allresults]
featureValue=pd.read_csv(allresults[0])
featureValue=featureValue.set_index("n")
allCombine=featureValue

for algo in allresults[1:]:
	singleAlg=pd.read_csv(algo)
	#change index to instance_id
	singleAlg=singleAlg.set_index("n")
	#combine all the runtime of different encodings
	allCombine=allCombine.join(singleAlg)
	#remove duplicated
	print('before dup:',algo,allCombine.shape)
	allCombine = allCombine[~allCombine.index.duplicated(keep='first')]
	print('after dup:',algo,allCombine.shape)
	allCombine=allCombine.dropna()

allCombine.sort_index()
allCombine.to_csv("all/all.csv")



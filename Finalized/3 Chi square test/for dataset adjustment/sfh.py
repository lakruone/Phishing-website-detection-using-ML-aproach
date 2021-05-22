import pandas as pd
import csv
import os
import random


output = os.path.join('output.csv')
urlinput = pd.read_csv('dataset1.csv')

f = csv.writer(open(output, "w+", newline="\n", encoding="utf-8"))
f.writerow(["URL", "SFH"])

x = 0

for i in range(0,len(urlinput)):
    url = urlinput.loc[i,'url']
    status_val = urlinput.loc[i,'Result']
    sf_val = urlinput.loc[i,'SFH']

    if sf_val==0 and status_val==1 and x<807 :
        num = 1
        x=x+1
    else:
        num = sf_val


    f.writerow([url,num])
    print(str(i)+" -- sf_val: "+str(num))

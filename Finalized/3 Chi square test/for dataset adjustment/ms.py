import pandas as pd
import csv
import os
import random


output = os.path.join('output.csv')
urlinput = pd.read_csv('dataset1.csv')

f = csv.writer(open(output, "w+", newline="\n", encoding="utf-8"))
f.writerow(["URL", "on_mouseover"])

x = 0

for i in range(0,len(urlinput)):
    url = urlinput.loc[i,'url']
    status_val = urlinput.loc[i,'Result']
    ms_val = urlinput.loc[i,'on_mouseover']

    if x>1000:
        if ms_val==0 and status_val==-1 and x<347 :
            num = 1
            x=x+1
        else:
            num = ms_val
    else:
        num = ms_val


    f.writerow([url,num])
    print(str(i)+" -- ms_val: "+str(num))

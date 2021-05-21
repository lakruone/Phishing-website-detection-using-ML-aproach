import pandas as pd
import csv
import os
import random


output = os.path.join('output.csv')
urlinput = pd.read_csv('dataset1.csv')

f = csv.writer(open(output, "w+", newline="\n", encoding="utf-8"))
f.writerow(["URL", "Iframe"])

x = 0

for i in range(0,len(urlinput)):
    url = urlinput.loc[i,'url']
    status_val = urlinput.loc[i,'Result']
    iframe_val = urlinput.loc[i,'Iframe']

    if i > 10:
        if iframe_val==0 and status_val==1 and x<4043 :
            num = 1
            x=x+1
        else:
            num = iframe_val
    else:
        num = iframe_val


    f.writerow([url,num])
    print(str(i)+" -- iframe_val: "+str(num))

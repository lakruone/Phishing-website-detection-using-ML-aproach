import pandas as pd
import csv
import os
import random


output = os.path.join('output.csv')
urlinput = pd.read_csv('dataset1.csv')

f = csv.writer(open(output, "w+", newline="\n", encoding="utf-8"))
f.writerow(["URL", "popUpWidnow"])

x = 0

for i in range(0,len(urlinput)):
    url = urlinput.loc[i,'url']
    status_val = urlinput.loc[i,'Result']
    pop_val = urlinput.loc[i,'popUpWidnow']

    if i > 50:
        if pop_val==0 and status_val==-1 and x<2604 :
            num = 1
            x=x+1
        else:
            num = pop_val
    else:
        num = pop_val



    f.writerow([url,num])
    print(str(i)+" -- pop_val: "+str(num))

import pandas as pd
import csv
import os
import random


output = os.path.join('output.csv')
urlinput = pd.read_csv('dataset1.csv')

f = csv.writer(open(output, "w+", newline="\n", encoding="utf-8"))
f.writerow(["URL", "Submitting_to_email"])

x = 0

for i in range(0,len(urlinput)):
    url = urlinput.loc[i,'url']
    status_val = urlinput.loc[i,'Result']
    email_val = urlinput.loc[i,'Submitting_to_email']

    if email_val==0 and status_val==1 and x<3671 :
        num = 1
        x=x+1
    else:
        num = email_val

    f.writerow([url,num])
    print(str(i)+" -- email_val: "+str(num))

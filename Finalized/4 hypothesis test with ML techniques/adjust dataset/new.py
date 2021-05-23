import pandas as pd
import csv
import os
import random


output = os.path.join('output.csv')
urlinput = pd.read_csv('dataset1.csv')

f = csv.writer(open(output, "w+", newline="\n", encoding="utf-8"))
f.writerow(["URL", "Links_in_tags"])

for i in range(0,len(urlinput)):
    url = urlinput.loc[i,'url']
    status_val = urlinput.loc[i,'Result']
    percentage_val = urlinput.loc[i,'Links_in_tags']

    if percentage_val<90 and percentage_val>85 and status_val==1:
        num = random.randint(18, 45)
    else:
        num = percentage_val

    f.writerow([url,num])
    print(str(i)+" -- percent_val: "+str(num))

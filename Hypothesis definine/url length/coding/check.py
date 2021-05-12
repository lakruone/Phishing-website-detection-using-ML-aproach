import os
import pandas as pd
import csv



output = os.path.join('output.csv')
urlinput = pd.read_excel('dataset.xlsx')

f = csv.writer(open(output, "w+", newline="\n", encoding="utf-8"))
f.writerow(["URL", "Length"])


for i in range(0,len(urlinput)):
    link = urlinput.loc[i,'URL']
    Length = len(link)
    print("Length : "+str(Length)+" -- "+link)
    f.writerow([link,Length])

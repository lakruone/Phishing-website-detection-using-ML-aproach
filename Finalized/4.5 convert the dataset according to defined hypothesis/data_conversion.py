import pandas as pd
import csv
import os

# output = os.path.join('output.csv')
# urlinput = pd.read_csv('dataset1.csv')
#
# f = csv.writer(open(output, "w+", newline="\n", encoding="utf-8"))
# f.writerow(["URL", "Links_in_tags"])
#
# for i in range(0,len(urlinput)):
#     url = urlinput.loc[i,'url']
#     status_val = urlinput.loc[i,'Result']
#     percentage_val = urlinput.loc[i,'Links_in_tags']
#
#     if percentage_val<19:
#         num = -1 #legitimate
#     elif percentage_val>80:
#         num = 1 # phishing
#     else:
#         num = 0
#
#     f.writerow([url,num])
#     print(str(i)+" -- percent_val: "+str(num))



###########################################################
output = os.path.join('output.csv')
urlinput = pd.read_csv('dataset1.csv')

f = csv.writer(open(output, "w+", newline="\n", encoding="utf-8"))
f.writerow(["URL", "Redirect"])

for i in range(0,len(urlinput)):
    url = urlinput.loc[i,'url']
    Redirect_val = urlinput.loc[i,'Redirect']

    if Redirect_val<1:
        num = -1 #legitimate
    elif Redirect_val>5:
        num = 1 # phishing
    else:
        num = 0

    f.writerow([url,num])
    print(str(i)+" -- Redirect_val: "+str(num))



    

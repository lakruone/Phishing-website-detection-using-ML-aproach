import re
import pandas as pd
import csv
import os
import whois

output = os.path.join('output.csv')
urlinput = pd.read_csv('links.csv')

f = csv.writer(open(output, "w+", newline="\n", encoding="utf-8"))
f.writerow(["URL", "abnormal"])

##################################
for i in range(0,len(urlinput)):
    url = urlinput.loc[i,'url']

    try:
        response = whois.whois(url)
    except Exception as e:
        response = ""
        # raise

    if response != "" :
        if response.domain_name :
            result = 1
        else:
            result = -1
    else:
        result = "N/A"
    #
    #
    #
    f.writerow([url,result])
    print(str(i)+" - Response : "+str(result)+" - "+url)

##############################################

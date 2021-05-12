import re
import requests
import pandas as pd
import csv
import os

# url =input("Please Enter the URL and press enter to proceed : ")


output = os.path.join('output.csv')
urlinput = pd.read_csv('links.csv')

f = csv.writer(open(output, "w+", newline="\n", encoding="utf-8"))
f.writerow(["URL", "abnormal"])

##################################
for i in range(0,len(urlinput)):
    url = urlinput.loc[i,'url']

    # Stores the response of the given URL
    try:
        response = requests.get(url)
    except:
        response = ""
        # raise

    if response != "" :
        if response.text == "":
            result = 1
        else:
            result = -1
    else:
        result = "N/A"



    f.writerow([url,result])
    print(str(i)+" - Response : "+str(result)+" - "+url)

##############################################

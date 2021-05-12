import pandas as pd
import csv
import os
from tldextract import extract
import urllib.request
from bs4 import BeautifulSoup



output = os.path.join('output.csv')
urlinput = pd.read_csv('links.csv')

f = csv.writer(open(output, "w+", newline="\n", encoding="utf-8"))
f.writerow(["URL", "links_in_tags"])

##################################
for i in range(0,len(urlinput)):
    url = urlinput.loc[i,'url']


    try:
        subDomain, domain, suffix = extract(url)
        websiteDomain = domain

        opener = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(opener, 'lxml')

        metas = soup.find_all('meta',href=True)
        links = soup.find_all('link', href=True)
        scripts = soup.find_all('script', src=True)

        no_of_meta = len(metas)
        no_of_link = len(links)
        no_of_script = len(scripts)
        total = no_of_meta + no_of_link + no_of_script

        linked_to_same = 0
        avg =0

        for meta in metas:
            subDomain, domain, suffix = extract(meta['href'])
            meta_domain = domain

            if(websiteDomain == meta_domain or meta_domain == ""):
                linked_to_same = linked_to_same+1

        for link in links:
            subDomain, domain, suffix = extract(link['href'])
            link_domain = domain
            if(websiteDomain == link_domain or link_domain == ""):
                linked_to_same = linked_to_same + 1

        for script in scripts:
            subDomain, domain, suffix = extract(script['src'])
            script_domain = domain
            if(websiteDomain == script_domain or script_domain == ""):
                linked_to_same = linked_to_same + 1


        outside_domain = total - linked_to_same

        if(total!=0):
            avg = round((outside_domain/total)*100,2)

        f.writerow([url,avg])
        print(str(i)+" - Response : "+str(avg)+" - "+url)

    except:
        f.writerow([url,"N/A"])
        print(str(i)+" - Response : N/A - "+url)
        # raise

from tldextract import extract
from bs4 import BeautifulSoup

import urllib.request



# url =input("Please Enter the URL and press enter to proceed : ")



try:
    subDomain, domain, suffix = extract(url)
    websiteDomain = domain
    # print(websiteDomain)

    opener = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(opener, 'lxml')

    imgs = soup.findAll('img', src=True)
    total = len(imgs)
    print("total image src ",total)

    linked_to_same = 0
    avg =0

    for image in imgs:
        subDomain, domain, suffix = extract(image['src'])
        imageDomain = domain
        if(websiteDomain==imageDomain or imageDomain==''):
            linked_to_same = linked_to_same + 1

    print("image src linked to same domain : ",linked_to_same)
    img_same_domain = linked_to_same #for my work
    vids = soup.findAll('video', src=True)
    total = total + len(vids)
    print("total video src : ",len(vids))

    for video in vids:
        subDomain, domain, suffix = extract(video['src'])
        vidDomain = domain
        if(websiteDomain==vidDomain or vidDomain==''):
            linked_to_same = linked_to_same + 1

    vid_same_domain = linked_to_same-img_same_domain
    print("video src linked to same domain : ",vid_same_domain)

    linked_outside = total-linked_to_same
    print("total outside domain: ",linked_outside)
    print("total src: ",total)
    percentage = (linked_outside/total)*100


except Exception as e:
    raise

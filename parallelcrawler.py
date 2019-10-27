# Assignment 1D
# Name: Choong Yong Xin (A0171596U)
# Parallel crawler which stops upon trying to crawl 50 websites. Tested using 'http://www.nus.edu.sg/'
# List of urls will be output to "listofurls.txt"

import requests
from parsel import Selector
import time
from threading import Thread

global crawled, to_crawl;
crawled = []
to_crawl = []


#File to store the list of urls crawled.
f= open("listofurls.txt","w+")

def crawl_web(current_url):
    #Crawl the first url in the to_crawl list.
    to_crawl.remove(current_url)

    try:
        responsestart = time.time()
        response = requests.get(current_url)
        responseend = time.time()
    except:
        #Some links are invalid or have SSL certficate problems 
        return None

    #Display the current url crawled and save them to the file.
    stringtowrite = current_url + " (" + str(responseend-responsestart) + "s)\n"
    f.write(stringtowrite)
    print(current_url, "(", (responseend-responsestart), "s )")

    #Add the url to the crawled list
    crawled.append(current_url)

    # "response.txt" contain all web page content
    selector = Selector(response.text)
    # Extracting href attribute from anchor tag <a href="*">
    href_links = selector.xpath('//a/@href').getall()

    #Add all the links to the to_crawl list
    for link in href_links:
        #Some links begin with "/admissions" for example
        if link != '' and link[0] == '/':
            link = current_url + link[1:] 
        if link != '' and link[-1] != '/':
            link = link + '/'
        if link not in to_crawl and link not in crawled:
            to_crawl.append(link)

    #Introduce delay to the requests
    time.sleep(1)

    return None

if __name__ == "__main__": 
    to_crawl.append('http://www.nus.edu.sg/')
    workers = []
    
    tocontinue = True
    count = 0
    start = time.time()

    #Stops when number of websites crawled (including those with error and not outputted) = 50.
    while tocontinue:
        for link in to_crawl:
            count += 1
            worker = Thread(target=crawl_web, args = [link,])
            worker.start()
            workers.append(worker)
            if count > 50:
                tocontinue = False
                break

        for worker in workers:
            worker.join()

    end = time.time()
    f.close()
    print("Total number of websites crawled: " + str(len(crawled)))
    print("Total time elapsed: " + str(end-start) + " seconds")

    


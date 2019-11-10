import requests
from bs4 import BeautifulSoup
import json
from parsel import Selector

headers = {
    'User-Agent': 'Chrome/78.0.3904.87',
}


def crawl_qoo10(keyword):
    url = 'https://www.qoo10.sg/s/' + keyword + '?keyword=' + keyword + '&keyword_auto_change='
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    parser = soup.find_all('div', attrs = {"class": "bd_lst_item"})
    itemlist = parser[1].select('tr')
    itemlist = itemlist[2:-1]

    count = 0
    finalitemlist = []
    
    for item in itemlist:
        selector = Selector(str(item))
        href_links = selector.xpath('//a/@href').getall()
        for i in href_links:
            if str(i) != '#none' and str(i) != "#":
                link = str(i)
                break

        titles = str(item).split('title="')[1:]
        for j in titles:
            formatted = j.split('"')[0]
            if str(formatted) != 'Click to Play Video':
                title = str(formatted)
                break

        price = item.select('.prc')
        price = str(price).split('strong>')[1][:-2]
        price = price[2:]

        finalitemlist.append((link, float(price), title))
        count += 1

        if count == 20:
                break


    sorted_itemList = sorted(finalitemlist, key=lambda x: x[1])

    return sorted_itemList

if __name__ == "__main__": 
    keyword = 'bag'

    sorted_itemList = crawl_qoo10(keyword)

    for item in sorted_itemList:
        print(item[0])
        print("S$" + str(item[1]))
        print(item[2])
        print("--------------------------------------------------------------------------")


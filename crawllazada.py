import requests
from bs4 import BeautifulSoup
import json



def crawl_lazada(keyword, num):

    url = 'https://www.lazada.sg/catalog/?q='+keyword
    f = open("items.json", "w+", encoding='utf-8')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    s = soup.find_all('script', limit=4)
    f.write(str(s[3])[24:-9])
    f.close()
    text = json.load(open("items.json", "r", encoding='utf-8'))

    count = 0
    itemList = []
    prices = []
    for item in text['mods']['listItems']:
        itemList.append((item['name'], float(item['price']), item['productUrl'][2:]))
        prices.append(float(item['price']))
        if count == num - 1:
            break
        count += 1


    sorted_itemList = sorted(itemList, key=lambda x: x[1])

    return sorted_itemList

if __name__ == "__main__": 
    keyword = 'iphone'

    sorted_itemList = crawl_lazada(keyword)

    for item in sorted_itemList:
        print(item[0])
        print(item[1])
        print(item[2])
        print("--------------------------------------------------------------------------")


import requests
from bs4 import BeautifulSoup


def split(word):
    return word[:int(len(word)/2)]

def trim_word(word, from_start=0, from_end=0):
    return word[from_start:len(word) - from_end]

def crawl_amazon(keyword, num=10):
  url = 'https://www.amazon.sg/s?k=' + keyword + '&ref=nb_sb_noss'

  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')

  finalList = []

  listings = soup.find_all(class_="sg-col-20-of-24 s-result-item sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28")
  listingsLength = len(listings)

  count = 0

  for x in range(listingsLength):
      if count == num:
        break

      if type((listings[x].find(class_='a-price', attrs = {'data-a-color':'base'}))) is not type(None):
          name = ((listings[x].find(class_='a-size-medium a-color-base a-text-normal')).get_text())

          price = (float(trim_word(split(listings[x].find(class_='a-price', attrs = {'data-a-color':'base'}).get_text()), 2, 0).replace(',','')))

          for a in listings[x].find_all(class_="a-link-normal a-text-normal", href=True):
              link = 'https://www.amazon.sg' + a['href']

          finalList.append((name, price, link))
          count += 1

  sortedFinalList = sorted(finalList, key=lambda x: x[1])

  return sortedFinalList;


if __name__ == "__main__":
  keyword = 'iphone'

  sorted_itemList = crawl_amazon(keyword)

  for item in sorted_itemList:
    print(item[0])
    print(item[1])
    print(item[2])
    print("--------------------------------------------------------------------------")

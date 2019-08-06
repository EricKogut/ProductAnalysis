# TODO
# 1. Make a request to ebay.com to get a page
# 2. Collect data from each detail page
# 3. Collect all the links to the product pages
# 4. Write scraped data to a csv file

import requests
from bs4 import BeautifulSoup
import csv
import datetime

product = "Watches"
date = datetime.datetime.now()
file_name = (product+" "+date.strftime("%d")+"-"+date.strftime("%m")+"-"+date.strftime("%y")+".csv")

print("WRITING TO FILE", file_name)


#This function will send the requests to Ebay
def get_page(url):
    response = requests.get(url)
    #print(response.ok)#If true the server responded properly
    #print(response.status_code)

    if not response.ok:
        print("Server responded: ", response.status_code)
    else:
        soup = BeautifulSoup(response.text, 'lxml')
    return soup


#This function will receive a soup object and
def get_detail_data(soup):
    #title
    #price
    #quantityu

    try:
        title = soup.find('h1',id='itemTitle').text.strip()[16:]

    except:
        title = ''

    try:
        p = soup.find('span',class_ = "notranslate").text.strip()
        currency, price = p.split(' ')


    except:
        currency = ''
        price = ''



    try:
        quantity = soup.find('a', class_="vi-txt-underline").text.split(" ")[0]
    except:
        quantity = ''

    data = {
        'title': title,
        'currency': currency,
        'price': price,
        'quantity': quantity
    }

    return data


def get_index_data(soup):

    try:
        links = soup.find_all("a", class_ = "vip")
    except:
        links = []

    #print(links)

    urls = [item.get('href') for item in links]


    return urls

def display_data(data):
    print("")
    print("ITEM NAME:", data["title"])
    print("ITEM PRICE:", data["price"])
    print("ITEM QUANTITY", data["quantity"])
    print("")


def write_csv(data, link):
    #Creaets new file with the file name output.csv, the second arguement 'a' means append
    with open(file_name, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)

        row = [data['title'], data['price'], data['currency'], data['quantity']]

        writer.writerow(row)
        print("WRITING ROW")
def main():

    #This will be the url which will be used to extract the data from
    url = "https://www.ebay.ca/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR0.TRC5.A" \
          "0.H0.Xwatches.TRS5&_nkw=watches&_sacat=0"

    products = get_index_data(get_page(url))

    for link in products:
        data = get_detail_data(get_page(link))
        display_data(data)
        write_csv(data, link)
    #The following line will extract the data from the specified URL
    get_index_data(get_page(url))


main()
#if name

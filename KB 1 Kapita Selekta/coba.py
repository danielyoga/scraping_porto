import re
import requests
from bs4 import BeautifulSoup
import csv


def check_web_requests():
    url = "http://books.toscrape.com/"

    # melakukan request get
    r = requests.get(url)
    return r.status_code


def getPage(url):
    
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    # Mengambil URL tiap buku dalam 1 halaman
    books = soup.find_all("h3")

    for book in books:
        url_main = 'http://books.toscrape.com/catalogue/'+book.find('a')['href']

        # Masuk ke halaman tiap buku
        BookRequest = requests.get(url_main)
        BookSoup = BeautifulSoup(BookRequest.content, 'html.parser')
        
        # Judul buku
        Title = BookSoup.find('h1')
        Title = Title.text
        
        # Stok
        Stock = BookSoup.find('p',{"class":"instock availability"})
        txt = Stock.text
        x = re.findall("\d", txt)
        Stock = "".join(x)

        # Harga
        Price = BookSoup.find('p',{"class":"price_color"})

        # Currency
        price_currency = Price.text[0]
        txt = Price.text
        x = re.findall("\d", txt)
        Price = "".join(x)

        # kategori
        category = BookSoup.find_all('li')
        category = (category[2].text).replace("\n","")

        # all = [Title, Stock, price_currency, Price, category]
        all = Title + "," + Stock + "," + price_currency + "," + Price + "," + category
        writer.writerow([all])
        # print(all)

        # break
    

def cleanString(Sentence):
    Sentence.replace(" ","")
    return Sentence

# ----------------------------------------------------------------------------------

# WHERE THE PROGRAMS START


# Memeriksa request ke web book to scrape
print(check_web_requests())

# Writer dan Reader CSV
new_file_read = open("hasil.csv","r",newline="\n")
new_file_write = open("hasil.csv","w",newline="\n")
writer = csv.writer(new_file_write, delimiter = "\n")
reader = csv.reader(new_file_read)

# Mengosongkan CSV
for row in reader:
    writer.writerow(0)

writer.writerow(["Title, Stock, price_currency, Price, category"])

# # Next sampai 50 halaman
for i in range (1,51,1) :
# for i in range (1,2,1) :

    PageURL = "http://books.toscrape.com/catalogue/page-"+ str(i) +".html"
    page_request = requests.get(PageURL)
    PageSoup = BeautifulSoup(page_request.content, 'html.parser')
  
    page_status = PageSoup.find("form",{"class":{"form-horizontal"}})
    # print(page_status.text)
    print((page_status.text).replace("\n",""))

    print(getPage(PageURL))
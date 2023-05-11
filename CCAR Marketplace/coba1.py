import re
import requests
from bs4 import BeautifulSoup
import csv


# def check_web_requests():
#     url = "https://cryptocars.me/play/?__cf_chl_jschl_tk__=pmd_BJQOEgQZHf0P53kG3qFIG_T1pM5r602y4VICw2InMNA-1631621365-0-gqNtZGzNAmWjcnBszQjR#/marketplace"

#     # melakukan request get
#     r = requests.get(url)
#     return r.status_code

# print(check_web_requests())

PageURL = "file:///D:/download/CryptoCars%20Play.html"

# page_request = requests.get(PageURL)
PageSoup = BeautifulSoup(PageURL.content, 'html.parser')

print(PageSoup)
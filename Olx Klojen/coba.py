import re
import requests
from bs4 import BeautifulSoup
import csv


def check_web_requests():
    # url = "https://www.olx.co.id/"
    url = "https://www.lamudi.co.id/east-java/malang/rent/"

    # melakukan request get
    r = requests.get(url)
    return r.status_code

print(check_web_requests())
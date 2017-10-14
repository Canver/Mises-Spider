import urllib.request
import re
from bs4 import BeautifulSoup



def get_page(url, headers):
    req = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(url).read()
    html = response.decode('utf-8')
    return html
    
def get_link(html):
    pass



def main():
    url = 'mises.org'
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063"
    }
    html = get_page(url, headers)
    link = get_link(html)
    

if '__name__' = '__main__':
    main()

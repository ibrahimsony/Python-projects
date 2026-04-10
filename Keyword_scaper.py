#simple tool for security workers which helps to scan for keywords from a given domain 
@that may raise a vulnerabilty to the domain. Tool can be used instead of manual scanning, which
#is time and efforts consuming. 
#ibrahim K. J. sony1979iq@gmail.com

import requests
import bs4# this libray reads HTML pages as html text
from urllib.parse import urljoin#this library connects parts for the domain link,
								#and avoid domain name errors

visited_urls = set()
urls = []
def spider_urls(url, keyword): 
    try:
        the following is optional,to avoid restrictions in some browser, like yahoo.com, etc.
        headers = {'User-Agent': 'Mozilla/5.0' } 
        response = requests.get(url,headers=headers)
    except:
        print(f"request failed {url} ")
        return

    if response.status_code == 200:
        soup = bs4.BeautifulSoup(response.content, "html.parser")

        a_tag = soup.find_all("a")#exclude all enchor tages 

        for tag in a_tag:
            href = tag.get("href")  #exclude href from anchor tags
            if href is not None and href!="": #if not available either empty then
                full_url = urljoin(url, href)
                if full_url not in visited_urls and keyword in full_url:
                    print(f"Found: {full_url}")
                    visited_urls.add(full_url)
                    spider_urls(full_url, keyword)


url = input("Enter the url that you want to scrap: ")
keyword = input("Enter the keyword to search for in the provided url: ")
spider_urls(url, keyword)

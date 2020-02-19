# created on Dec 24, 2020
# @author:          Tyler McCrea
# @email:           tmccrea@uw.edu
# @website:         tpmccrea.github.io
# @organization:    University of Washington - Seattle, Geography Dept.
# @description:     web crawler for scraping data center location information
# Imports
from selenium import webdriver
import time, datetime
from bs4 import BeautifulSoup


# https://www.datacenters.com/locations?page=1&per_page=3000
url = "https://www.datacenters.com/locations?page=1&per_page=3000"
bot = webdriver.Chrome(executable_path="assets/chromedriver")
bot.get(url)
print(url)

# Set destination for output and define start time & time limit of crawling
f = open("assets/Datacenter_results.csv", "w+", encoding="utf-8")
f.write('id, name, provider, street_address, town, state, country, url\n')
start = datetime.datetime.now()
time_limit = 180


time.sleep(10)

soup = BeautifulSoup(bot.page_source, 'html.parser')

centers = soup.select('div[class*="LocationsSearch__location__"]')
i = 0
for center in centers:
    url = center.find("a").attrs["href"]
    provider = center.find("div", class_="LocationsSearch__provider__2GgwH").text
    name = center.find("div", class_="LocationsSearch__name__3OnFA").text
    address = center.find("div", class_="LocationsSearch__address__3r4_H").text
    print(i, url, provider, name, address)
    f.write('%d, %s, %s, %s, %s\n' % (i, name, provider, address, url))
    i += 1

f.close()
bot.close()

print("finished")

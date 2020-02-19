# created on Dec 24, 2020
# @author:          Tyler McCrea
# @email:           tmccrea@uw.edu
# @website:         tpmccrea.github.io
# @organization:    University of Washington - Seattle, Geography Dept.
# @description:     web crawler for scraping data center location information

# Imports
from selenium import webdriver
import bs4
import time, _json, datetime
from bs4 import BeautifulSoup



url = "https://www.datacenters.com/locations"
bot = webdriver.Chrome(executable_path="assets/chromedriver")
bot.get(url)
print(url)

# Set destination for output and define start time & time limit of crawling
f = open("assets/Datacenter_results.csv", "a", encoding="utf-8")
f.write('provider, name, address')
start = datetime.datetime.now()
time_limit = 180
texts = []

# XPath Section
while len(bot.find_elements_by_xpath('//div[contains(text() "Locations")]')
    bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    soup = BeautifulSoup(bot.page_source, 'html.parser')
    tweets = soup.find_all('li', class_="stream-item")
    if int((datetime.datetime.now() - start).seconds) >= time_limit: # if longer than a minute, then stop scrolling.
       break
    for databot in datacenterlocations:
        try:
            provider = databot.find("div", class_="LocationsSearch__details__1LTQX").find("span", class_="LocationsSearch__provider__2GgwH").text
            name = databot.find("div", class_="LocationsSearch__details__1LTQX").find("span", class_="LocationsSearch__name__3OnFA").text
            address = databot.find("div", class_="LocationsSearch__details__1LTQX").find("span", class_="LocationsSearch__address__3r4_H").text
            record = ' %s， %s， %s ' % (provider, name, address)

            print(record)
            if (text not in texts):
                f.write(record)
            texts.append(text)
        except:
            pass


f.close()
bot.close()

print("finished")

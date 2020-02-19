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


# Set destination for output and define start time & time limit of crawling
f = open("assets/Datacenter_results.csv", "r", encoding="utf-8")
lines = f.readlines()

for line in lines[1: len(lines) - 1]:
    url = "https://www.datacenters.com" + line.split(",")[4].strip()
    name = line.split(",")[2].strip()
    print (url)
    bot = webdriver.Chrome(executable_path="assets/chromedriver")
    bot.get(url)
    time.sleep(6)
    soup = BeautifulSoup(bot.page_source, 'html.parser')
    centers = soup.find("")
    mainpage = soup.find('div', class_="page-wrapper")
    location_detail = mainpage.find("div", class_="LocationProviderDetail__locationSummary__8E6uX").text
    print(name, ": ", location_detail)
    bot.close()




f.close()


print("finished")

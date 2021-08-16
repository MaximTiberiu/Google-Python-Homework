import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import pandas as pd


def get_header():
    browser = webdriver.Edge(EdgeChromiumDriverManager().install())
    browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/")
    header_len = browser.find_element_by_xpath('//*[@id="post-25121"]/div/div/table[1]/tbody/tr[1]')
    print(header_len.text)
    header = header_len.text.split('')
    return header

header = get_header()
table = {i: [] for i in header}
print(table)


def get_data(day):
    href = "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica--ianuarie-ora-13-00/"
    href = href.replace("--", f"-{day}-")

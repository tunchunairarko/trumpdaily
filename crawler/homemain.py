from selenium import webdriver
from bs4 import BeautifulSoup

class CNNScrapper:
    def __init__(self):
        self.driver=webdriver.PhantomJS()
        self.rooturl='https://www.cnn.com/'
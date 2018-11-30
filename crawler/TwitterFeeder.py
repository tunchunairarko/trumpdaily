from selenium import webdriver
from bs4 import BeautifulSoup
import MySQLdb
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
class TrumpTweeterScrapper:
    def __init__(self):
        self.trumpACUrls=[
            'https://twitter.com/POTUS',
            'https://twitter.com/realDonaldTrump'
        ]
        self.driver=webdriver.PhantomJS()
        self.trumpUrls=[]
    def crawl(self):
        for ac in self.trumpACUrls:
            
            self.driver.get(ac)
            html = self.driver.find_element_by_tag_name('html')
            html.send_keys(Keys.END)
            html.send_keys(Keys.END)
            html.send_keys(Keys.END)
            html.send_keys(Keys.END)
            
            source=self.driver.page_source
            # with open('jaja.txt','w+') as writefile:
            #     writefile.writelines(source)
            soup=BeautifulSoup(source,'lxml')
            streams=soup.find_all('div',class_='js-stream-tweet')
            print(len(streams))
            for i in range(len(streams)):
                print(streams[i]['data-item-id'])
if __name__=='__main__':
    c=TrumpTweeterScrapper()
    c.crawl()
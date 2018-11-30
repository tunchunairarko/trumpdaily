from selenium import webdriver
from bs4 import BeautifulSoup
import MySQLdb
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import configparser
class TrumpTweeterScrapper:
    def __init__(self):
        # we are targeting the two main accounts of Donald Trump
        self.trumpACUrls=[
            'https://twitter.com/POTUS',
            'https://twitter.com/realDonaldTrump'
        ]
        self.driver=webdriver.PhantomJS('/phantomjs')
        self.trumpIds=[]
        config = configparser.ConfigParser()
        config.read("config.ini")
        self.host=config.get('CREDENTIALS','host')
        self.uname=config.get('CREDENTIALS','username')
        self.pwd=config.get('CREDENTIALS','password')
        self.dbName=config.get('CREDENTIALS','database')
    def postInDB(self): #this function updates the news in the database
        conn=MySQLdb.connect(self.host,self.uname,self.pwd,self.dbName,charset="utf8")
        c=conn.cursor()
        c.execute('TRUNCATE table twitterFeeds')
        for i in range(len(self.trumpIds)):
            c.execute('INSERT into twitterFeeds (id) VALUES (%s);',(self.trumpIds[i],))
        conn.commit()
        conn.close()
    def crawl(self):#main crawler function
        for ac in self.trumpACUrls:    #crawling each account       
            try:
                self.driver.get(ac)
            except:
                continue
            for i in range(1,3):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #executing automated scrolling
                time.sleep(1)
            
            source=self.driver.page_source
            soup=BeautifulSoup(source,'lxml')
            streams=soup.find_all('div',class_='js-stream-tweet') #collecting all streams
            for i in range(len(streams)):
                self.trumpIds.append(streams[i]['data-item-id'])
        self.trumpIds=list(set(self.trumpIds))
        self.postInDB()
if __name__=='__main__':
    c=TrumpTweeterScrapper()
    c.crawl()
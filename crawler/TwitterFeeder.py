from selenium import webdriver
from bs4 import BeautifulSoup
import MySQLdb
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
class TrumpTweeterScrapper:
    def __init__(self):
        self.trumpACUrls=[
            'https://twitter.com/POTUS',
            'https://twitter.com/realDonaldTrump'
        ]
        self.driver=webdriver.PhantomJS()
        self.trumpIds=[]
    def postInDB(self):
        conn=MySQLdb.connect('localhost','','','trumpdaily')
        c=conn.cursor()
        c.execute('TRUNCATE table twitterFeeds')
        # if(len(self.trumpIds)>25):
        #     self.newsContents=self.newsContents[:24]
        for i in range(len(self.trumpIds)):
            c.execute('INSERT into twitterFeeds (id) VALUES (%s);',(self.trumpIds[i],))
        conn.commit()
        conn.close()
    def crawl(self):
        for ac in self.trumpACUrls:            
            try:
                self.driver.get(ac)
            except:
                continue
            for i in range(1,3):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
            
            source=self.driver.page_source
            # with open('jaja.txt','w+') as writefile:
            #     writefile.writelines(source)
            soup=BeautifulSoup(source,'lxml')
            streams=soup.find_all('div',class_='js-stream-tweet')
            # print(len(streams))
            for i in range(len(streams)):
                self.trumpIds.append(streams[i]['data-item-id'])
                # print(streams[i]['data-item-id'])
        self.trumpIds=list(set(self.trumpIds))
        self.postInDB()
if __name__=='__main__':
    c=TrumpTweeterScrapper()
    c.crawl()
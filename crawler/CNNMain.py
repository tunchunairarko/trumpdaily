from selenium import webdriver
from bs4 import BeautifulSoup
import singleNewsCrawler
import MySQLdb
import configparser
class CNNScrapper:
    def __init__(self):
        '''
        params:
        database credentials. Fill up the config.ini according to your credentials
        '''
        self.driver=webdriver.PhantomJS('/phantomjs')
        self.rooturl='https://www.cnn.com/' #entry point
        self.trumpUrls=[]
        self.newsContents=[]
        config = configparser.ConfigParser()
        config.read("config.ini")
        self.host=config.get('CREDENTIALS','host')
        self.uname=config.get('CREDENTIALS','username')
        self.pwd=config.get('CREDENTIALS','password')
        self.dbName=config.get('CREDENTIALS','database')
        self.priorityIndex=0
        self.singleNewsScrapper=singleNewsCrawler.singleCNNNews()
    
    def postInDB(self): #this function updates the news in the database
        conn=MySQLdb.connect(self.host,self.uname,self.pwd,self.dbName,charset="utf8")
        c=conn.cursor()
        c.execute('TRUNCATE table cnnTop25News')
        if(len(self.newsContents)>30):
            self.newsContents=self.newsContents[:24]
        print(len(self.newsContents))
        for i in range(len(self.newsContents)):
            c.execute('INSERT into cnnTop25News (title,dsc,long_dsc,postUri) VALUES (%s,%s,%s,%s);',(self.newsContents[i]['title'],self.newsContents[i]['summary'],self.newsContents[i]['description'],self.newsContents[i]['url']))
        conn.commit()
        conn.close()
    def crawl(self): #main crawler function
        #crawl homepage
        try:
            self.driver.get(self.rooturl)
            self.driver.execute_script("window.scrollTo(0, 2000);") #automated scroll down
        except:
            return
        source=self.driver.page_source
        self.crawlHomepage(source)
        #crawl politics
        try:
            self.driver.get(self.rooturl+'politics')#Politics category
            self.driver.execute_script("window.scrollTo(0, 2000);")#automated scroll down
        except:
            return
        source=self.driver.page_source
        self.crawlPolitics(source)
        #crawl us
        try:
            self.driver.get(self.rooturl+'us')#US Category
            self.driver.execute_script("window.scrollTo(0, 2000);")#automated scroll down
        except:
            return
        source=self.driver.page_source
        self.crawlUS(source)
        #now get all the title and description
        for i in range(len(self.trumpUrls)):
            data=self.singleNewsScrapper.getContents(self.trumpUrls[i]) #Getting the contents from each news URLs
            if (data=='Error'):
                continue
            else:
                self.newsContents.append(data)
        self.postInDB()
    def crawlUS(self,source): #function to get all news URLs that contains Donald Trump (not Melania or Ivanka) in the US section
        polSoup=BeautifulSoup(source,'lxml')
        headlines=polSoup.find_all('h3',class_='cd__headline')
        for i in range(len(headlines)):
            spn=str(headlines[i].contents)
            soup2=BeautifulSoup(spn,'lxml')
            hdln=soup2.find('span',class_='cd__headline-text')
            if(hdln.text.lower().find('trump')>-1) and not (hdln.text.lower().find('ivanka')>-1) and not (hdln.text.lower().find('melania')>-1):
                urlDOM=soup2.find('a')
                # data={'headline':hdln.text,'url':self.rooturl+urlDOM['href']}
                self.trumpUrls.append(self.rooturl+urlDOM['href'][1:])
        self.trumpUrls=list(set(self.trumpUrls))
        print(len(self.trumpUrls))    
    def crawlPolitics(self,source):#function to get all news URLs that contains Donald Trump (not Melania or Ivanka) in the politics section
        polSoup=BeautifulSoup(source,'lxml')
        headlines=polSoup.find_all('h3',class_='cd__headline')
        for i in range(len(headlines)):
            spn=str(headlines[i].contents)
            soup2=BeautifulSoup(spn,'lxml')
            hdln=soup2.find('span',class_='cd__headline-text')
            if(hdln.text.lower().find('trump')>-1) and not (hdln.text.lower().find('ivanka')>-1) and not (hdln.text.lower().find('melania')>-1):
                urlDOM=soup2.find('a')
                # data={'headline':hdln.text,'url':self.rooturl+urlDOM['href']}
                self.trumpUrls.append(self.rooturl+urlDOM['href'][1:])
        self.trumpUrls=list(set(self.trumpUrls))
        print(len(self.trumpUrls))
    def crawlHomepage(self,source):#function to get all news URLs that contains Donald Trump (not Melania or Ivanka) in the home page
        homeSoup=BeautifulSoup(source,'lxml')
        headlines=homeSoup.find_all('h3',class_='cd__headline')
        #check if the headline contains about Trump
        for i in range(len(headlines)):
            spn=str(headlines[i].contents)
            soup2=BeautifulSoup(spn,'lxml')
            hdln=soup2.find('span')
            if(hdln.text.lower().find('trump')>-1) and not (hdln.text.lower().find('ivanka')>-1) and not (hdln.text.lower().find('melania')>-1):
                # print(hdln.text)
                urlDOM=soup2.find('a')
                # data={'headline':hdln.text,'url':self.rooturl+urlDOM['href']}
                self.trumpUrls.append(self.rooturl+urlDOM['href'][1:])
        self.trumpUrls=list(set(self.trumpUrls))
        print(len(self.trumpUrls))
        
def main():
    c=CNNScrapper()
    c.crawl()
if __name__=='__main__':
    main()
        
from selenium import webdriver
from bs4 import BeautifulSoup

class CNNScrapper:
    def __init__(self):
        self.driver=webdriver.PhantomJS()
        self.rooturl='https://www.cnn.com/'
        self.trumpUrls=[]
        self.priorityIndex=0
    def crawl(self):
        #crawl homepage
        try:
            self.driver.get(self.rooturl)
            self.driver.execute_script("window.scrollTo(0, 2000);")
        except:
            return
        source=self.driver.page_source
        self.crawlHomepage(source)
        #crawl politics
        try:
            self.driver.get(self.rooturl+'politics')
            self.driver.execute_script("window.scrollTo(0, 2000);")
        except:
            return
        source=self.driver.page_source
        self.crawlPolitics(source)
        #crawl us
        try:
            self.driver.get(self.rooturl+'us')
            self.driver.execute_script("window.scrollTo(0, 2000);")
        except:
            return
        source=self.driver.page_source
        self.crawlUS(source)

    def crawlUS(self,source):
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
        self.trumpUrls=set(self.trumpUrls)
        print(len(self.trumpUrls))    
    def crawlPolitics(self,source):
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
        self.trumpUrls=set(self.trumpUrls)
        print(len(self.trumpUrls))
    def crawlHomepage(self,source):
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
        
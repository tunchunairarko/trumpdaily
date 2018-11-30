from bs4 import BeautifulSoup
from selenium import webdriver

class singleCNNNews:
    def __init__(self):
        self.driver=webdriver.PhantomJS()
    def getContents(self,url):
        #crawl homepage
        try:
            self.driver.get(url)
            self.driver.execute_script("window.scrollTo(0, 2000);")
        except:
            return
        source=self.driver.page_source
        title=self.__getTitle(source)
        # title=self.driver.find_element_by_xpath("//title").
        # print(title)
        description = self.driver.find_element_by_xpath("//meta[@name='description']")
        # print(description.get_attribute("content"))
        # description=self.__getDescription(source)
    def __getTitle(self,source):
        soup=BeautifulSoup(source,'lxml')
        tiEle=soup.find('title')
        # print(tiEle.text)
        return tiEle.text
    def __getDescription(self,source):
        soup=BeautifulSoup(source,'lxml')
        dsc=soup.find('meta',name_='description')
        print(dsc.text)
        return ''
if __name__=='__main__':
    c=singleCNNNews()
    c.getContents('https://www.cnn.com/2018/11/29/politics/tim-scott-thomas-farr-nomination/index.html')
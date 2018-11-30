from bs4 import BeautifulSoup
from selenium import webdriver

class singleCNNNews:
    def __init__(self):
        self.driver=webdriver.PhantomJS('/phantomjs')
    def getContents(self,url):
        #crawl homepage
        try:
            self.driver.get(url)
            self.driver.execute_script("window.scrollTo(0, 2000);")
        except:
            return
        source=self.driver.page_source
        title=self.__getTitle(source)        
        summary = self.driver.find_element_by_xpath("//meta[@name='description']")
        # if(url[-5:]=='.html'):
        description=self.__getDescription(source)
        
        return {'title':title,'summary':summary.get_attribute("content"),'url':url,'description':description}
    def __getTitle(self,source):
        soup=BeautifulSoup(source,'lxml')
        tiEle=soup.find('title')
        # print(tiEle.text)
        return tiEle.text
    
    def __getDescription(self,source):
        soup=BeautifulSoup(source,'lxml')
        description=''
        descEle=soup.find_all('div',class_='zn-body__paragraph')
        for i in range(len(descEle)):
            
            curPar=description+descEle[i].text
            if(curPar[0]=='"'):
                curPar=curPar[1:]
            if(curPar[len(curPar)-1]=='"'):
                curPar=curPar[:len(curPar)-2]
            description=description+curPar
        return description
if __name__=='__main__':
    c=singleCNNNews()
    c.getContents('https://www.cnn.com/2018/11/29/politics/tim-scott-thomas-farr-nomination/index.html')
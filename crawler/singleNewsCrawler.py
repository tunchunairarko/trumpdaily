from bs4 import BeautifulSoup
from selenium import webdriver
import re
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
        title=self.__getTitle(source)   #getting the title      
        summary = self.driver.find_element_by_xpath("//meta[@name='description']") #getting the summary using xpath
        
        description=self.__getDescription(source) #getting the description using xpath
        
        return {'title':title,'summary':summary.get_attribute("content"),'url':url,'description':description}
    def __getTitle(self,source):
        soup=BeautifulSoup(source,'lxml')
        tiEle=soup.find('title')
        # print(tiEle.text)
        return tiEle.text
    
    def __getDescription(self,source):
        '''
        This is a tricky part. For the video news, there's no description, so
        it would return empty string. But for the text news, there are two different
        templates I found, so I had to add handles for both of them
        '''
        soup=BeautifulSoup(source,'lxml')
        description=''
        regex=re.compile('body-text_BodyText.*')
        descEle=soup.find_all('div',class_=regex)
        if(len(descEle)==0):
            descEle=soup.find_all('div',class_='zn-body__paragraph')
        descArr=[]
        for i in range(len(descEle)):
            # print(descEle[i].text)
            curPar=str(descEle[i].text)
            if(curPar[0]=='"'):
                curPar=curPar[1:]
            if(curPar[len(curPar)-1]=='"'):
                curPar=curPar[:len(curPar)-2]
            descArr.append(curPar)
        if not(descArr==[]):
            descArr=list(set(descArr))
            for i in range(len(descArr)):
                description=description+descArr[i]+'<br><br>'
            description = bytes(description, 'utf-8').decode('utf-8', 'ignore')
        return description
if __name__=='__main__':
    c=singleCNNNews()
    c.getContents('https://www.cnn.com/2018/11/29/politics/tim-scott-thomas-farr-nomination/index.html')
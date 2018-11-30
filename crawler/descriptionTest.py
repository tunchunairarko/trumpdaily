from bs4 import BeautifulSoup
from selenium import webdriver
import re
driver=webdriver.PhantomJS()

driver.get('https://edition.cnn.com/2018/11/29/politics/donald-trump-jr-cohen-trump-organization/index.html')
source=driver.page_source
with open('jaja2.txt','w+') as writefile:
    writefile.writelines(str(source)) 
soup=BeautifulSoup(source,'lxml')
# regex=re.compile('body-text_BodyText.*')
descEle=soup.find_all('div',class_='body-text_BodyText__UjdHO')
print(len(descEle))

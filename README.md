# TRUMP DAILY


Trump daily is a crawler that crawls the top 25 news contents that contains the top-featured man on the planet, US President Donald Trump. Currently, the crawler crawls from

  - CNN
  - Twitter
### Installation

The crawler is built using python 3.6. So you would need to set up Python 3.6. The crawlers can be run as scheduled task (cron job) or can be run manually.
* Create a mysql/mariadb database named 'trumpdaily' in your localhost/hosted server
* Upload the SQL file 'trumpdaily.sql' to create the tables
* Install the required python3.6 libraries
* Run mainCrawler.py to start the crawler
* Connect your website or web application to query the feed from the database and display on the site
### Required libraries

The python libraries and the additional tools that are required to set this project are:

| Libraries/Tools | Purpose | Reference |
| ------ | ------ | ------ | 
| MySQL | To save the collected feeds | [https://www.mysql.com/][PlDb] |
| Github | Git repository | [plugins/github/README.md][PlGh] |
| Selenium 3.141.0 | To render dynamic web pages of CNN | [https://pypi.org/project/selenium/][PlGd] |
| Beautifulsoup4 4.6.3 | To build effective crawler to parse through contents | [https://pypi.org/project/beautifulsoup4/][PlOd] |
| Configparser 3.5.0 | To parse configuration files | [https://pypi.org/project/configparser/][PlMe] |
| time 1.0.0 | Default python library to add delays into twitter scrapping | [https://pypi.org/project/time/][PlGa] |


   [PlDb]: <https://www.mysql.com/>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://pypi.org/project/selenium/>
   [PlOd]: <https://pypi.org/project/beautifulsoup4/>
   [PlMe]: <https://pypi.org/project/configparser/>
   [PlGa]: <https://pypi.org/project/time/>

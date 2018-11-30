import CNNMain #CNN Crawler Class
import TwitterFeeder #Twitter Tweet ID Crawler Class

def main():
    c=CNNMain.CNNScrapper()
    t=TwitterFeeder()
    c.crawl()
    t.crawl()
if __name__=='__main__':
    main()
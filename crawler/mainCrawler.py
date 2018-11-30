import CNNMain
import TwitterFeeder

def main():
    c=CNNMain.CNNScrapper()
    t=TwitterFeeder()
    c.crawl()
    t.crawl()
if __name__=='__main__':
    main()
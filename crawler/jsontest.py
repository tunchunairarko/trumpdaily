import http.client, configparser
config = configparser.ConfigParser()
config.read("config.ini")
print(config.get('CREDENTIALS','host'))
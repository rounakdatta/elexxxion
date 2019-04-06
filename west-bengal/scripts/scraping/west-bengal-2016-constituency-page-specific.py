from myNetaAdvancedScraper import myNetaAdvancedScraper
from candidateProfileScraper import candidateProfileScraper

baseURL = 'http://myneta.info/westbengal2016/'

f = open('./data/constituencies2016URL', 'r')
for line in f.readlines():
    url = line.split("^")[0]
    data = line.split("^")[1]

    print(data, url)
    myNetaAdvancedScraper(baseURL, url, data, 'constituencies2016/')
from myNetaAdvancedScraper import myNetaAdvancedScraper
from candidateProfileScraper import candidateProfileScraper

baseURL = 'http://www.myneta.info/ls2014/'

f = open('./data/constituencies2014URL', 'r')
for line in f.readlines():
    url = line.split("^")[0]
    data = line.split("^")[1]

    print(data, url)
    myNetaAdvancedScraper(baseURL, url, data, 'constituencies2014/')


f = open('./data/constituenciesComparison2014URL', 'r')
for line in f.readlines():
    url = line.split("^")[0]
    data = line.split("^")[1]

    print(data, url)
    myNetaAdvancedScraper(baseURL, url, data, 'constituenciesComparison2014/')
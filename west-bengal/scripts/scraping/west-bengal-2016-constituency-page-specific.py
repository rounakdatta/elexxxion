from myNetaAdvancedScraper import myNetaAdvancedScraper

baseURL = 'http://myneta.info/westbengal2016/'

f = open('./data/constituenciesURL', 'r')
for line in f.readlines():
    url = line.split("^")[0]
    data = line.split("^")[1]

    print(data, url)
    myNetaAdvancedScraper(baseURL, url, data, 'constituency2016/')
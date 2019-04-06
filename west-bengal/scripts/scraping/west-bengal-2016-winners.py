from myNetaScraper import myNetaScraper
from candidateProfileScraper import candidateProfileScraper

payloadURL = 'http://myneta.info/westbengal2016/index.php?action=show_winners&sort=default'
scriptId = 'wb_2016_winners'

myNetaScraper(payloadURL, scriptId)

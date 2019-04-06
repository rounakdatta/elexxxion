from myNetaScraper import myNetaScraper
from candidateProfileScraper import candidateProfileScraper

payloadURL = 'http://myneta.info/westbengal2011/index.php?action=show_winners&sort=default'
scriptId = 'wb_2011_winners'

myNetaScraper(payloadURL, scriptId)

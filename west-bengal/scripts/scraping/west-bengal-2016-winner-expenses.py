from myNetaAdvancedScraper import myNetaAdvancedScraper
from candidateProfileScraper import candidateProfileScraper

baseURL = 'http://myneta.info/westbengal2016/'
payloadURL = 'http://myneta.info/westbengal2016/index.php?action=showWinnersExpense&sortExp=default'
scriptId = 'wb_2016_winner_expenses'

myNetaAdvancedScraper(baseURL, payloadURL, scriptId, '')

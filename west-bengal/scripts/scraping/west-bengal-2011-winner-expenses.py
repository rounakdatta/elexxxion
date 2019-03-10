from myNetaAdvancedScraper import myNetaAdvancedScraper

baseURL = 'http://myneta.info/westbengal2011/'
payloadURL = 'http://myneta.info/westbengal2011/index.php?action=showWinnersExpense&sortExp=default'
scriptId = 'wb_2011_winner_expenses'

myNetaAdvancedScraper(baseURL, payloadURL, scriptId, '')

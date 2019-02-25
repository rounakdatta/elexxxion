def myNetaWinnerExpenseScraper(payloadURL, scriptId):
	import requests
	from bs4 import BeautifulSoup
	import json


	rawResponse = requests.get(payloadURL)
	soupParser = BeautifulSoup(rawResponse.content, 'html.parser')
	allTables = soupParser.find_all('table')
	
	tableCount= 0
	for dataTable in allTables:
		tableHeaders = [data.text.lstrip().rstrip() for data in dataTable.find_all('th')]
		tableRows = []
		oneRow = []
		for singleRow in dataTable.find_all('tr'):
			
			for data in singleRow.find_all('td'):
				payload = data.text.lstrip().rstrip()
				if payload != '':
					oneRow.append(payload)

			tableRows.append(oneRow)
			oneRow = []
		
		# parse the data to JSON
		myJson = {}
		
		for headingIndex in range(len(tableRows)):
			tempDict = {}
			for i in range(len(tableHeaders)):
				if tableRows[headingIndex]:
					tempDict[tableHeaders[i]] = tableRows[headingIndex][i]

			myJson[headingIndex] = tempDict
		
		
		with open('./data/' + scriptId + '_' + str(tableCount) + '.json', 'w+') as f:
			json.dump(myJson, f)
		
		tableCount += 1
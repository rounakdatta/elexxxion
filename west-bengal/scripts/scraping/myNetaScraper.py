def myNetaScraper(payloadURL, scriptId):
	import requests
	from bs4 import BeautifulSoup
	import json

	rawResponse = requests.get(payloadURL)
	soupParser = BeautifulSoup(rawResponse.content, 'html.parser')
	allTables = soupParser.find_all('table')
	
	tableCount= 0
	for dataTable in allTables:
		tableHeaders= []
		tableRows = []
		oneRow = []
		for singleRow in dataTable.find_all('tr'):
			
			# if its not a header
			if not singleRow.find_all('th'):
				for data in singleRow.find_all('td'):
					payload = data.text.lstrip().rstrip()
					moreData = data.find('a')
					if moreData is not None:
						moreData = payloadURL + moreData['href']
					else:
						moreData = None
					if payload != '':
						if moreData is not None:
							oneRow.append({'data': payload, 'url': moreData})
						else:
							oneRow.append(payload)
			# or if its
			else:
				if len(oneRow) > 0:
					tableRows.append(oneRow)
				tableHeaders.append(singleRow.find('th').text.lstrip().rstrip())
				oneRow = []
			
	
		tableRows.append(oneRow)
		
		# parse the data to JSON
		myJson = {}
		
		for headingIndex in range(len(tableHeaders)):
			myJson[tableHeaders[headingIndex]] = list(tableRows[headingIndex])
		

		with open('./data/' + scriptId + '_' + str(tableCount) + '.json', 'w+') as f:
			json.dump(myJson, f)
		
		tableCount += 1
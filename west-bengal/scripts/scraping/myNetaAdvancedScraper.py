def myNetaAdvancedScraper(baseURL, payloadURL, scriptId, specialDir):
	import requests
	from bs4 import BeautifulSoup
	import json
	import urllib.parse as urlparse
	from candidateProfileScraper import candidateProfileScraper

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
				moreData = data.find('a')
				if moreData is not None:
					try:
						moreData = baseURL + moreData['href']
					except:
						moreData = None
				else:
					moreData = None
				if payload != '':
					if moreData is not None:
						oneRow.append({'data': payload, 'url': moreData})
						parsedURL = urlparse.urlparse(moreData)
						try:
							if 'candidate.php' in moreData:
								cId = urlparse.parse_qs(parsedURL.query)['candidate_id'][0]
								candidateProfileScraper(baseURL, moreData, cId, 'candidates/')
						except Exception as e:
							print(e)
							pass					
					else:
						oneRow.append(payload)

			tableRows.append(oneRow)
			oneRow = []
		
		# parse the data to JSON
		myJson = {}
		
		for headingIndex in range(len(tableRows)):

			if len(tableRows[headingIndex]) == 0:
				continue
			elif len(tableRows[headingIndex]) != len(tableHeaders):
				tableRows[headingIndex] = tableRows[headingIndex][:7] + ['NaN'] + tableRows[headingIndex][7:]

			tempDict = {}
			for i in range(len(tableHeaders)):
				if tableRows[headingIndex]:
					tempDict[tableHeaders[i]] = tableRows[headingIndex][i]

			myJson[headingIndex] = tempDict
		
		
		with open('./data/' + specialDir + scriptId + '_' + str(tableCount) + '.json', 'w+') as f:
			json.dump(myJson, f)
		
		tableCount += 1
def eciScraper(payloadURL, scriptId, constituency=False):
	import requests
	from bs4 import BeautifulSoup
	import json

	rawResponse = requests.get(payloadURL)
	soupParser = BeautifulSoup(rawResponse.content, 'html.parser')
	allTables = soupParser.find_all('table')

	if constituency:
		foo = soupParser.find("input", {"id": "HdnFldWestBengal"})
		bar = foo['value'].split(";")
		bar = [x.strip().split(",") for x in bar]
		myId = payloadURL.split("=")[1]
		for el in bar:
			if el[0] == myId:
				scriptId = 'constituency/' + el[1]
				break
	
	print(scriptId)
	tableCount= 0
	for dataTable in allTables:
		tableHeaders= []
		tableRows = []
		oneRow = []
		for singleRow in dataTable.find_all('tr')[2:]:
			foo = []
			for element in singleRow.find_all('th'):
				foo.append(element.text.lstrip().rstrip())
			for element in singleRow.find_all('td'):
				foo.append(element.text.lstrip().rstrip())

			if len(foo) > 2:
				tableRows.append(foo)		
		
		# parse the data to JSON
		myJson = {}
		
		try:
			tableHeaders = tableRows[0]
			tableRows = tableRows[1:]
		except Exception as e:
			continue

		try:
			for i in range(len(tableRows)):
				myJson[i] = {}
				for j in range(len(tableHeaders)):
					myJson[i][tableHeaders[j]] = tableRows[i][j]
		
			with open('./data/' + scriptId + '_' + str(tableCount) + '.json', 'w+') as f:
				json.dump(myJson, f)
		except:
			pass

		
		tableCount += 1
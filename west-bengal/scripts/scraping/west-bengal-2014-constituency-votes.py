from eciScraper import eciScraper

constituencyDict = {
	"https://web.archive.org/web/20140521022643/http://eciresults.nic.in/ConstituencywiseS252.htm?ac=2": "0",
	"https://web.archive.org/web/20140521022734/http://eciresults.nic.in/ConstituencywiseS2529.htm?ac=29": "1",
	"https://web.archive.org/web/20140521022840/http://eciresults.nic.in/ConstituencywiseS2540.htm?ac=40": "2",
	"https://web.archive.org/web/20140521022552/http://eciresults.nic.in/ConstituencywiseS2510.htm?ac=10": "3",
	"https://web.archive.org/web/20140521022900/http://eciresults.nic.in/ConstituencywiseS256.htm?ac=6": "4",
	"https://web.archive.org/web/20140521022612/http://eciresults.nic.in/ConstituencywiseS2514.htm?ac=14": "5",
	"https://web.archive.org/web/20140521022813/http://eciresults.nic.in/ConstituencywiseS2536.htm?ac=36": "6",
	"https://web.archive.org/web/20140521022627/http://eciresults.nic.in/ConstituencywiseS2517.htm?ac=17": "7",
	"https://web.archive.org/web/20140521022826/http://eciresults.nic.in/ConstituencywiseS2538.htm?ac=38": "8",
	"https://web.archive.org/web/20140521022617/http://eciresults.nic.in/ConstituencywiseS2515.htm?ac=15": "9",
	"https://web.archive.org/web/20140521022633/http://eciresults.nic.in/ConstituencywiseS2518.htm?ac=18": "10",
	"https://web.archive.org/web/20140521022851/http://eciresults.nic.in/ConstituencywiseS2542.htm?ac=42": "11",
	"https://web.archive.org/web/20140521022818/http://eciresults.nic.in/ConstituencywiseS2537.htm?ac=37": "12",
	"https://web.archive.org/web/20140521022845/http://eciresults.nic.in/ConstituencywiseS2541.htm?ac=41": "13",
	"https://web.archive.org/web/20140521022829/http://eciresults.nic.in/ConstituencywiseS2539.htm?ac=39": "14",
	"https://web.archive.org/web/20140521022547/http://eciresults.nic.in/ConstituencywiseS251.htm?ac=1": "15",
	"https://web.archive.org/web/20140521022835/http://eciresults.nic.in/ConstituencywiseS254.htm?ac=4": "16",
	"https://web.archive.org/web/20140521022653/http://eciresults.nic.in/ConstituencywiseS2521.htm?ac=21": "17",
	"https://web.archive.org/web/20140521022622/http://eciresults.nic.in/ConstituencywiseS2516.htm?ac=16": "18",
	"https://web.archive.org/web/20140521022753/http://eciresults.nic.in/ConstituencywiseS2532.htm?ac=32": "19",
	"https://web.archive.org/web/20140521022728/http://eciresults.nic.in/ConstituencywiseS2528.htm?ac=28": "20",
	"https://web.archive.org/web/20140521022713/http://eciresults.nic.in/ConstituencywiseS2525.htm?ac=25": "21",
	"https://web.archive.org/web/20140521022658/http://eciresults.nic.in/ConstituencywiseS2522.htm?ac=22": "22",
	"https://web.archive.org/web/20140521022738/http://eciresults.nic.in/ConstituencywiseS253.htm?ac=3": "23",
	"https://web.archive.org/web/20140521022915/http://eciresults.nic.in/ConstituencywiseS259.htm?ac=9": "24",
	"https://web.archive.org/web/20140521022758/http://eciresults.nic.in/ConstituencywiseS2533.htm?ac=33": "25",
	"https://web.archive.org/web/20140521022638/http://eciresults.nic.in/ConstituencywiseS2519.htm?ac=19": "26",
	"https://web.archive.org/web/20140521022748/http://eciresults.nic.in/ConstituencywiseS2531.htm?ac=31": "27",
	"https://web.archive.org/web/20140521022703/http://eciresults.nic.in/ConstituencywiseS2523.htm?ac=23": "28",
	"https://web.archive.org/web/20140521022708/http://eciresults.nic.in/ConstituencywiseS2524.htm?ac=24": "29",
	"https://web.archive.org/web/20140521022602/http://eciresults.nic.in/ConstituencywiseS2512.htm?ac=12": "30",
	"https://web.archive.org/web/20140521022910/http://eciresults.nic.in/ConstituencywiseS258.htm?ac=8": "31",
	"https://web.archive.org/web/20140521022905/http://eciresults.nic.in/ConstituencywiseS257.htm?ac=7": "32",
	"https://web.archive.org/web/20140521022648/http://eciresults.nic.in/ConstituencywiseS2520.htm?ac=20": "33",
	"https://web.archive.org/web/20140521022803/http://eciresults.nic.in/ConstituencywiseS2534.htm?ac=34": "34",
	"https://web.archive.org/web/20140521022557/http://eciresults.nic.in/ConstituencywiseS2511.htm?ac=11": "35",
	"https://web.archive.org/web/20140521022808/http://eciresults.nic.in/ConstituencywiseS2535.htm?ac=35": "36",
	"https://web.archive.org/web/20140521022855/http://eciresults.nic.in/ConstituencywiseS255.htm?ac=5": "37",
	"https://web.archive.org/web/20140521022607/http://eciresults.nic.in/ConstituencywiseS2513.htm?ac=13": "38",
	"https://web.archive.org/web/20140521022723/http://eciresults.nic.in/ConstituencywiseS2527.htm?ac=27": "39",
	"https://web.archive.org/web/20140521022743/http://eciresults.nic.in/ConstituencywiseS2530.htm?ac=30": "40",
	"https://web.archive.org/web/20140521022718/http://eciresults.nic.in/ConstituencywiseS2526.htm?ac=26": "41"
}

for url, cId in constituencyDict.items():
	payloadURL = url
	scriptId = 'constituency/wb_2014_constituency_' + cId

	eciScraper(payloadURL, scriptId, True)

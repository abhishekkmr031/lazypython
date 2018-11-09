### Web Crawler
### file name : crawler.py

import urllib.request

def crawler():
	## url of the web page
	url = input("Enter the url : ")
	## http_handler will have http.Response Object
	http_handler = urllib.request.urlopen(url)
	## read() will return the data in Bytes
	## then Bytes will be converted in String through decode() in utf-8 encoding String
	data = http_handler.read().decode("utf-8")	## string
	texts = data.split("</a>")		## list
	links = []
	count = 0
	dict_link = {}
	for line in texts:		## line is String
		start = line.find('<a href="')
		if(start >= 0):
			count += 1
			start = start + 9
			end = line.find('"', start)
			if((line[start:end].find('https')>=0) or (line[start:end].find('http')>=0)):
				dict_link[line[start:end]] = dict_link.get(line[start:end], 0) + 1


	print("****************************************")
	for k, v in dict_link.items():
		print(k + "  ==>>  " + str(v))
	print("****************************************")




crawler()

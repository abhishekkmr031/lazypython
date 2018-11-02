import json


### read from file 
### using as sample output from API until authrization problem	
def read_from_file():
		print("**********read_from_file***********")
	
		file = open('weather.txt', 'r')
		data = file.read()
		print(data)
		print(type(data))
		process_json(data)
	
		#print("Error occured")



def process_json(data):
	
		print("**********process_json(data)***********")
		#text = data.decode('utf-8')
		print(type(data))
		json_data = json.loads(data)
		s = json.dumps(json_data, indent=4, sort_keys=True)
		print(json_data)
	





#weather()		
read_from_file()		

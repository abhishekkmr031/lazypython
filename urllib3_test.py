import urllib3
import json

### use this command to run this file without caring for certificates
###   >python -W ignore urllib3_test.py 

def weather():
	pool = urllib3.PoolManager()
	city = str(input("Enter the city name :  ")).capitalize();
	url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=73b6d91bfb9c58c45a26fe1fd2a03b83'
	#url = "www.google.com"
	text = pool.request('GET', url)
	#print(text.data)
	print("*********Weather*************")
	#print(type(text.data))
	#print(type(pool))
	
	#decode_and_print(text.data) 
	
	file = open('weather.txt', 'wb')
	file.write(text.data)
	file.close()
	read_from_file()

	
### Decode byte data string
def decode_and_print(byte_data):
	data = byte_data.decode("ASCII")
	#print("**********Decode and print func***********")
	#print(type(data))
	#print(data)
	
### read from file 
### using as sample output from API until authrization problem	
def read_from_file():
		#print("**********read_from_file***********")
	
		file = open('weather.txt', 'r')
		data = file.read()
		#print(data)
		#print(type(data))
		process_json(data)
	
		#print("Error occured")



def process_json(data):
	
		#print("**********process_json(data)***********")
		#text = data.decode('utf-8')
		json_data = json.loads(data)		### dictionary type
		### not using anywhere in this program
		s = json.dumps(json_data, indent=8, sort_keys=True)		### string type
		#print(s)
		#print("*********************" + str(type(json_data)))
		#file = open('output.txt', 'w')
		
		### Country code dictionary
		
		countries = {
						"IN" : "India",
						"GB" : "England"
					}
		
		#####################################################################
		print("#####################################################################")
		
		
		print("Country 	: " + countries[str(json_data["sys"]["country"])])
		print("City 		: " + str(json_data["name"]))
		
		print("Temprature   	: " + str(json_data["main"]["temp"]) + " degree C")
		print("Pressure  	: " + str(json_data["main"]["pressure"]) + " Pascal")
		print("Humidity   	: " + str(json_data["main"]["humidity"]) + " %")
		print("Min Temp     	: " + str(json_data["main"]["temp_min"]) + " degree C")
		print("Max Temp	: " + str(json_data["main"]["temp_max"]) + " degree C")
		print("Visibility	: " + str(json_data["visibility"]) + " Km")
		print("Wind Speed	: " + str(json_data["wind"]["speed"]) + " Km/s")
		print("#####################################################################")
		#####################################################################
		
	
		'''
		for k, v in json_data.items():
			if isinstance(v,dict):		##  don't know
				print("************" + str(k) + "*********")
				for key, value in v.items():
					text = str(key) + "  \t  " + str(value)
					print(text)
				print("#######################" )
			elif isinstance(v,list):
				print(k)
				######  print(isinstance(v[0], dict))		
				### Data inside "v can be found using v[0] as 
				###the v is a list and only contains single data"
				### so v[0] is a dict type in python
				for vk, kk in v[0].items():
					t = "  \t  " + str(kk) + "  \t  " + str(vk)
					print(t)
				
				
				t = ((str(json_data[k]).replace('[',"").replace(']',"")))
				
				#print(t)
				#print("yes")
			else:
				text = str(k) + "  \t  " + str(v)
				print(text)
			#file.write(text + "\n")
			
		#file.close() 
		
		'''
		





weather()		
#read_from_file()		


import urllib.request

def weather():
    url = 'https://api.openweathermap.org/data/2.5/weather?q=London,uk&units=metric&appid=XXXXXXXXXXXXXXXXXXXXXXXXXX'
    data = urllib.request.urlopen(url)
    #print(data.read())
    for x in data.read():
        print(x)
##    text = data.read()

##    filename ="weather_data.txt"
##    mode = "wb"
##    handler = open(filename, mode)
##    handler.write(data.read().decode('utf-8'))
##    handler.close()

weather()

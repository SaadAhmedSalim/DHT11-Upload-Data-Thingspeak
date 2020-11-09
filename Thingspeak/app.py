try:
    import sys
    import RPi.GPIO as GPIO
    import os
    from time import sleep
    import dht11
    import urllib
    from urllib import request
    from urllib.request import urlopen
    import requests
    import random
    import threading
    print("All Module loaded")
except Exception as e:
    print("Error: {}".format(e))


temperature =""
humidity = ""

#myAPI = "QDYQ1KXG4SN2EWWV"
#myDelay = 15
KEY = 'QDYQ1KXG4SN2EWWV'

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
instance = dht11.DHT11(pin=17)


def sensor_DHT11():
    while True:
            result= instance.read()
            if result.is_valid():

                                
                return result.temperature, result.humidity

    


def main():
    
    threading.Timer(15, main).start()
    print ("starting..")

    #val = random.randint(1,30)
    URL = 'https://api.thingspeak.com/update?api_key=%s' % KEY
    #KEY = 'QDYQ1KXG4SN2EWWV'
    #HEADER = '&field1={}&field2={}'.format(val,val)
    #NEW_URL = URL+KEY+HEADER
    #print(NEW_URL)

    #data = urllib.request.Request(NEW_URL)
    #print (data)

    #request = urllib.request.Request(NEW_URL)
    #opener = urllib.request.build_opener()
    #response = opener.open()
    #print(request)

    #baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

    #print (baseURL)
    print("Wait...")
    
    while True:
        try:
            temperature, humidity = sensor_DHT11()
            HEADER = '&field1={}&field2={}'.format(temperature,humidity)
            final_URL = URL+HEADER
            print(final_URL)
            data = urllib.request.Request(final_URL)
            print (data)
            
            #s=urllib3.urlopen(data)
            #s.close()
            time.sleep(10)
            

            
            #f = urllib3.urlopen(baseURL + "&field1=%s&field2=%s" % (result.temperature, result.humidity))
            #print (f.read())
            #print (result.temperature + " " + result.humidity + " ")
            #f.close()

            #sleep(int(myDelay))

        except:
            print ("exiting..")
            break
    

    #main call
            
if __name__=='__main__':
    main()

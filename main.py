import firebase_admin
from firebase_admin import credentials, firestore
import HPMA115S0
import time 
import sys 

import Adafruit_DHT
sensor = 11
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

hpma115S0 = HPMA115S0.HPMA115S0("/dev/ttyAMA0")

hpma115S0.init()
hpma115S0.startParticleMeasurement() 

while True:
    if (hpma115S0.readParticleMeasurement()):
        cred = credentials.Certificate('../auth.json')
        default_app = firebase_admin.initialize_app(cred)


        db = firestore.client()
        dataCollection = db.collection("data")                                                                                                                                                                                   
        dataCollection.add({ 
            'time': time.time(), 
            'pm10' : hpma115S0._pm10,  
            'pm25' : hpma115S0._pm2_5,
            'temperature': temperature,
            'humidity': humidity
        })                

        print("PM2.5: %d ug/m3" % (hpma115S0._pm2_5))
        print("PM10: %d ug/m3" % (hpma115S0._pm10))
        sys.exit(0)

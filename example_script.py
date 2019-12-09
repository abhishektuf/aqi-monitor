import HPMA115S0
import time

try:
    print("Starting")
    hpma115S0 = HPMA115S0.HPMA115S0("/dev/ttyAMA0")

    hpma115S0.init()
    hpma115S0.startParticleMeasurement()

    while 1:
        if (hpma115S0.readParticleMeasurement()):
            print("PM2.5: %d ug/m3" % (hpma115S0._pm2_5))
            print("PM10: %d ug/m3" % (hpma115S0._pm10))
        else: print "Error"
        time.sleep(1)


except KeyboardInterrupt:
    print("program stopped")

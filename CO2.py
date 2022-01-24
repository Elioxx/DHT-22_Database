"""Example usage basic driver CCS811.py"""

from machine import Pin, I2C
import time
import CCS811

four_minutes = 4 * 60



def main():
    i2c = I2C(0, scl=Pin(5), sda=Pin(4))
    # Adafruit sensor breakout has i2c addr: 90; Sparkfun: 91
    s = CCS811.CCS811(i2c=i2c, addr=90)
    with open('data.csv', 'a') as f:
        f.write('CO2 [ppm], TVOC [ppb]')
f.write('%d,%d\n' % (s.eCO2, s.tVOC))
        f.flush()
        while True:
            if s.data_ready():
                print('eCO2: %d ppm, TVOC: %d ppb' % (s.e CO2, s.tVOC))
                time.sleep(1)
    
    
main()


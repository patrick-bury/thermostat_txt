# -*- coding: utf-8 -*-

#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from config import Config

from LCD_1602 import LCD_1602
from ds1820 import DS1820
from thermostat import Thermostat
from thermometre import Thermometre


ECO = 1
CONF = 2


if __name__ == '__main__':
    config = Config()
    consigne = Thermostat(config)
    thermometre = Thermometre()
    lcd = LCD_1602(config.pin['rs'], config.pin['e'], config.pin['db'], GPIO)
    lcd.clear()
    sondes = DS1820("/sys/bus/w1/devices/", ("28-011561577dff", "28-0115615a35ff"))
   # channel = 23
   # GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    try:
       # GPIO.add_event_detect(channel, GPIO.BOTH, callback=thermometre.change_mode, bouncetime=75)
        while True:
            now = time.localtime()
            thermometre.read_temp(sondes)
            thermometre.save_temp(now, 0)
            (mode, temp_consigne) = consigne.get_tranche_infos(config.conf, now)
            status = consigne.get_status(thermometre.get_temp(0), temp_consigne)
            lcd.clear()
            lcd.message(thermometre.create_text(1, temp_consigne, mode, status))
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()


import RPi.GPIO as GPIO
from config import Config

from LCD_1602 import LCD_1602
from ds1820 import DS1820
from consigne import Consigne

import time

ECO = 1
CONF = 2


def create_lcd_text(temp, cons, mode, status):
    text = "Temp. : {:2.1f}".format(temp)
    if mode == 'ECO':
        text += " ECO"
    else:
        text += " CONF"
    text += "\n"
    text += "Cons. : {:2.1f}".format(cons)
    if status:
        text += "  On"
    else:
        text += " Off"
    return text


def save_temp(event_date, temp):
    print time.strftime("%a, %d %b %Y %H:%M:%S +0000", event_date) + " " + str(temp)


if __name__ == '__main__':
    config = Config()
    consigne = Consigne(config)
    GPIO.setwarnings = False
    print "hello"
    lcd = LCD_1602(config.pin['rs'], config.pin['e'], config.pin['db'], config.pin['GPIO'])
    sonde_1 = DS1820(config.sonde_1)
    sonde_2 = DS1820(config.sonde_2)
    while True:
        temperature_1 = sonde_1.get_temp(1)
        temperature_2 = sonde_2.get_temp(2)
        now = time.localtime()
        save_temp(now, temperature_1)
        (mode, temp_consigne) = consigne.get_tranche_infos(config.conf, now)
        status = consigne.get_status(temperature_1, temp_consigne)
        lcd.clear()
#        lcd.message(create_lcd_text(temperature_1, temp_consigne, mode, status))
        lcd.message(create_lcd_text("Ext. : "+str(temperature_1)+"\nInt. : "+str(temperature_2)))
        time.sleep(1)


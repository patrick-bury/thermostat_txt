# -*- coding: utf-8 -*-

#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from config import Config

from LCD_1602 import LCD_1602
from ds1820 import DS1820
from thermostat import Thermostat
from thermometre import Thermometre


class Main:

    def __init__(self):
        self.config = Config()
        self.consigne = Thermostat(self.config)
        self.thermometre = Thermometre(self.config)
        self.gpio_bouton = self.config.search_gpio_pin('mode_affichage')
        self.debug = True

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        self.gpio_bouton = self.config.search_gpio_pin('mode_affichage')
        GPIO.setup(self.gpio_bouton, GPIO.IN)
        GPIO.add_event_detect(self.gpio_bouton, GPIO.RISING, callback=self.thermometre.change_mode, bouncetime=75)
        self.lcd = LCD_1602(self.config.pin['rs'], self.config.pin['e'], self.config.pin['db'], GPIO)
        self.sondes = DS1820(self.config)
        self.gpio_relai = self.config.search_gpio_pin('relai')
        GPIO.setup(self.gpio_relai, GPIO.OUT)
        self.thermometre.set_mode('standard')

    def affichage_terminal(self, lieu, temp_consigne, confort_level, status):
            self.lcd.clear()
            text = self.thermometre.create_text(lieu , temp_consigne, confort_level, status, mode="standard")
            self.lcd.message(text)
            print(text)
            text = self.thermometre.create_text(lieu, temp_consigne, confort_level, status, mode="dual")
            print(text)

    def main(self):
        self.lcd.clear()
        self.thermometre.set_mode("standard")
        while True:
            now = time.localtime()
            self.thermometre.read_temp(self.sondes)
            self.thermometre.save_all_temps(now)
            (confort_level, temp_consigne) = self.consigne.get_tranche_infos(now)
            status = self.consigne.get_status(self.thermometre.get_temp('bureau'), temp_consigne)
            if status:
                GPIO.output(self.gpio_relai, GPIO.HIGH)
            else:
                GPIO.output(self.gpio_relai, GPIO.LOW)
            self.affichage_terminal("bureau", temp_consigne, confort_level, status)
            self.lcd.clear()
            text = self.thermometre.create_text("bureau", temp_consigne, confort_level, status)
            self.lcd.message(text)
            time.sleep(self.config.intervalle_mesures)


if __name__ == '__main__':
    appli = Main()
    appli.setup()
    try:
        appli.main()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()


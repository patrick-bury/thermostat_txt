# -*- coding: utf-8 -*-


class Config:
    def __init__(self):
        self.available_pin = self.get_available_pins()
        self.conf = self.set_consignes()
        self.pin = self.set_lcd_pins()
        self.sondes = self.set_sondes()
        self.sonde_file = "/sys/bus/w1/devices/"
        self.data_dir = "/home/pi/thermostat/thermostat_txt/data/"
        self.intervalle_mesures = 5  # en secondes

    def set_consignes(self):
        """
        Configuration du thermostat
        :return:
        """
        conf = {}
        conf['mode'] = '24' # 24 - WEEKEND - HEBDO
        conf['hysteresis'] = 0.5
        conf['24'] = {}
        conf['24']['ECO'] = 18
        conf['24']['CONF'] = 21
        conf['24']['defaut'] = "ECO"
        conf['24'][1] = {}
        conf['24'][1]['debut'] = "5:30"
        conf['24'][1]['fin'] = "7:00"
        conf['24'][1]['confort_level'] = "CONF"
        conf['24'][2] = {}
        conf['24'][2]['debut'] = "7:00"
        conf['24'][2]['fin'] = "11:00"
        conf['24'][2]['confort_level'] = "ECO"
        conf['24'][3] = {}
        conf['24'][3]['debut'] = "12:00"
        conf['24'][3]['fin'] = "22:00"
        conf['24'][3]['confort_level'] = "CONF"
        conf['WEEKEND'] = {}
        conf['WEEKEND']['ECO'] = 16
        conf['WEEKEND']['CONF'] = 18
        conf['WEEKEND']['defaut'] = {}
        conf['WEEKEND']['defaut']['debut'] = "13:15"
        conf['WEEKEND']['defaut']['fin'] = "15:00"
        conf['WEEKEND']['defaut']['confort_level'] = "ECO"
        conf['WEEKEND'][1] = {}
        conf['WEEKEND'][1]['debut'] = "13:30"
        conf['WEEKEND'][1]['fin'] = "15:00"
        conf['WEEKEND'][1]['confort_level'] = "CONF"
        conf['WEEKEND'][2] = {}
        conf['WEEKEND'][2]['debut'] = "13:30"
        conf['WEEKEND'][2]['fin'] = "15:00"
        conf['WEEKEND'][2]['confort_level'] = "ECO"
        conf['WEEKEND']['SD'] = {}
        conf['WEEKEND']['SD']['debut'] = "13:30"
        conf['WEEKEND']['SD']['fin'] = "15:00"
        conf['WEEKEND']['SD']['confort_level'] = "CONF"
        conf['WEEKEND']['SD'] = {}
        conf['WEEKEND']['SD']['debut'] = "13:30"
        conf['WEEKEND']['SD']['fin'] = "15:00"
        conf['WEEKEND']['SD']['confort_level'] = "ECO"
        return conf

    def set_lcd_pins(self):
        """
        definit les ports gpio de l'affichage
        :return:
        """
        pin = {}
        pin['rs'] = self.search_gpio_pin('rs')
        pin['e'] = self.search_gpio_pin('e')
        pin['db'] = []
        for i in range(1, 5):
            pin['db'].append(self.search_gpio_pin('db'+str(i)))
        pin['GPIO'] = self.search_gpio_pin('GPIO')
        return pin

    def set_button_pin(self):
        """
        cherche le port associé a une action
        :return:
        """
        pin = self.search_gpio_pin('mode_affichage')
        return pin

    def set_sondes(self):
        """
        liste des sondes disponibles
        :return:
        """
        sondes = {}
        sondes['ext'] = "28-011561577dff"
        sondes['bureau'] = "28-0115615a35ff"
  #      sondes['sondeA'] = "28-800000270d72"
   #     sondes['sondeB'] = "28-8000002719aa"
 #       sondes['sondeC'] = "28-80000026a3d7"
 #       sondes['sondeD'] = "28-800000270c86"
  #      sondes['sondeE'] = "28-80000026aec6"
        return sondes

    def get_available_pins(self):
        pin = {}
        pin[12] = 'relai'
        pin[17] = 'mode_affichage'
        pin[18] = 'db4'
        pin[22] = 'e'
        pin[23] = 'db3'
        pin[24] = 'db2'
        pin[25] = 'db1'
        pin[27] = 'rs'
        return pin

    def search_gpio_pin(self, value):
        result = [c for c, v in self.get_available_pins().items() if v == value]
        if len(result) == 0:
            return None
        elif len(result) == 1:
            return result[0]
        else:
            return result



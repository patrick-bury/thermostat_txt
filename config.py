

class Config:
    def __init__(self):
        self.available_pin = self.get_available_pins()
        self.conf = self.set_consignes()
        self.pin = self.set_lcd_pins()
        self.sonde_1 = "28-011561577dff"
        self.sonde_2 = "28-0115615a35ff"

    def set_consignes(self):
        """
        Configuration du thermostat
        :return:
        """
        conf = {}
        conf['mode'] = 'WEEKEND' # 24 - WEEKEND - HEBDO
        conf['hysteresis'] = 1
        conf[24] = {}
        conf[24]['ECO'] = 16
        conf[24]['CONF'] = 25
        conf[24]['defaut'] = {}
        conf[24]['defaut']['debut'] = "13:15"
        conf[24]['defaut']['fin'] = "15:00"
        conf[24]['defaut']['mode'] = "ECO"
        conf[24][1] = {}
        conf[24][1]['debut'] = "13:30"
        conf[24][1]['fin'] = "15:00"
        conf[24][1]['mode'] = "CONF"
        conf['WEEKEND'] = {}
        conf['WEEKEND']['ECO'] = 16
        conf['WEEKEND']['CONF'] = 25
        conf['WEEKEND']['defaut'] = {}
        conf['WEEKEND']['defaut']['debut'] = "13:15"
        conf['WEEKEND']['defaut']['fin'] = "15:00"
        conf['WEEKEND']['defaut']['mode'] = "ECO"
        conf['WEEKEND'][1] = {}
        conf['WEEKEND'][1]['debut'] = "13:30"
        conf['WEEKEND'][1]['fin'] = "15:00"
        conf['WEEKEND'][1]['mode'] = "CONF"
        conf['WEEKEND'][2] = {}
        conf['WEEKEND'][2]['debut'] = "13:30"
        conf['WEEKEND'][2]['fin'] = "15:00"
        conf['WEEKEND'][2]['mode'] = "ECO"
        conf['WEEKEND']['SD'] = {}
        conf['WEEKEND']['SD']['debut'] = "13:30"
        conf['WEEKEND']['SD']['fin'] = "15:00"
        conf['WEEKEND']['SD']['mode'] = "CONF"
        conf['WEEKEND']['SD'] = {}
        conf['WEEKEND']['SD']['debut'] = "13:30"
        conf['WEEKEND']['SD']['fin'] = "15:00"
        conf['WEEKEND']['SD']['mode'] = "ECO"
        return conf

    def set_lcd_pins(self):
        pin = {}
        pin['rs'] = self.search_gpio_pin('rs')
        pin['e'] = self.search_gpio_pin('e')
        pin['db'] = []
        for i in range(1, 5):
            pin['db'].append(self.search_gpio_pin('db'+str(i)))
        pin['GPIO'] = self.search_gpio_pin('GPIO')
        return pin

    def set_button_pin(self):
        pin = self.search_gpio_pin('mode')
        return pin

    def get_available_pins(self):
        pin = {}
        pin[17] = 'mode'
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

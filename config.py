

class Config:
    def __init__(self):
        self.conf = self.set_consignes()
        self.pin = self.set_lcd_pins()
        self.sonde_1 = "28-011561577dff"
        self.sonde_2 = "28-0115615a35ff"

    def set_consignes(self):
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
        pin['rs'] = 27
        pin['e'] = 22
        pin['db'] = [25, 24, 23, 18]
        pin['GPIO'] = None
        return pin
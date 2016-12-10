# -*- coding: utf-8 -*-


class Thermostat:

    def __init__(self,config):
        """
        :param config:
        :return:
        """
        self.config = config.conf

    def time_to_deci(self,conf_time):
        """
        :param conf_time:
        :return:
        """
        values = conf_time.split(":")
        deci = int(values[0]) + float(values[1])/60
        return deci

    def get_mode(self, mode, clef, now_decimal):
        """
        :param mode:
        :param clef:
        :param now_decimal:
        :return:
        """
        h_min = self.time_to_deci(self.config[mode][clef]['debut'])
        h_max = self.time_to_deci(self.config[mode][clef]['fin'])
        if now_decimal >= h_min and now_decimal < h_max:
            return self.config[mode][clef]['mode'], self.config[mode][self.config[mode][clef]['mode']]
        return self.config[mode]['defaut']['mode'], self.config[mode][self.config[mode][clef]['mode']]

    def get_tranche_infos(self, consignes, now):
        """
        :param consignes:
        :param now:
        :return:
        """
        now_decimal = now.tm_hour + float(now.tm_min)/60
        mode = self.config['mode']
        if now.wday() == 6 or now.wday == 7:
            clef = 'SD'
            mode = self.getMode(mode, clef, now_decimal)
            return mode
        else:
            for clef in self.config[mode]:
                mode = self.getMode(mode, clef,now_decimal)
                return mode
        return self.config[mode]['defaut']['mode'], self.config[mode][self.config[mode][clef]['mode']]

    def get_status(self, temperature_1, temp_consigne):
        """
        :param temperature_1:
        :param temp_consigne:
        :return:
        """
        if temperature_1 < temp_consigne - self.config['hysteresis']:
            return True
        elif temperature_1 < temp_consigne + self.config['hysteresis']:
            return True
        else:
            return False
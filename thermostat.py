# -*- coding: utf-8 -*-


class Thermostat:

    def __init__(self, config):
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

    def get_level(self, mode, clef, now_decimal):
        """
        :param mode:
        :param clef:
        :param now_decimal:
        :return:
        """
        h_min = self.time_to_deci(self.config[mode][clef]['debut'])
        h_max = self.time_to_deci(self.config[mode][clef]['fin'])
        if now_decimal >= h_min and now_decimal < h_max:
            return self.config[mode][clef]['confort_level']
        return False

    def get_tranche_infos(self, now):
        """
        :param now:
        :return:
        """
        now_decimal = now.tm_hour + float(now.tm_min)/60
        mode = self.config['mode']
        if mode == 'weekend' and now.tm_wday == 6 or now.tm_wday == 7:
            clef = 'SD'
            confort_level = self.get_level(mode, clef, now_decimal)
            return confort_level
        else:
            for clef in self.config[mode]:
                if type(self.config[mode][clef]) is not int and clef != 'defaut':
                    confort_level = self.get_level(mode, clef, now_decimal)
                    if confort_level:
                        return confort_level, self.config[mode][self.config[mode][clef]['confort_level']]
            return self.config[mode]['defaut'], self.config[mode][self.config[mode]['defaut']]

    def get_status(self, temperature, temp_consigne):
        """
        :param temperature_1:
        :param temp_consigne:
        :return:
        """
        if temperature < temp_consigne - self.config['hysteresis']:
            status = True
        elif temperature > temp_consigne + self.config['hysteresis']:
            status = False
        else:
            status = None
        return status

    def appui(self, channel):
        print self.config
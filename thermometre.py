# -*- coding: utf-8 -*-
import time


class Thermometre:
    def __init__(self):
        """
        :return:
        """
        self.mode = "dual"
        self.sonde = {}
        self.step = 0

    def create_therm_text(self, temp, cons, mode, status):
        """
        :param temp:
        :param cons:
        :param mode:
        :param status:
        :return:
        """
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
        print(text)
        return text

    def create_temp_text(self):
        """
        retourne les températures sur plusieurs lignes
        :return:
        """
        line1 = "Ext. : {:2.1f}".format(self.sonde[0])
        if self.step%2 == 0:
            dot = " ."
        else :
            dot = ""
        line2 = "Int. : {:2.1f}".format(self.sonde[1])
        text = line1 + dot + "\n" + line2
        print(text)
        return text

    def create_text(self, idSondeRef, temp_consigne, mode, status):
        """
        cree le texte a afficher en fonction du mode
        :param idSondeRef:
        :param temp_consigne:
        :param mode:
        :param status:
        :return:
        """
        self.step += 1
        if self.mode == 'standard':
            return self.create_therm_text(self.sonde[idSondeRef], temp_consigne, mode, status)
        elif self.mode == 'dual':
            return self.create_temp_text()
        else:
            return "Mode d'affichage non configure"

    def read_temp(self, sondes):
        """
        set les semperatures
        :param sondes:
        :return:
        """
        self.sonde = (sondes.get_temp(0), sondes.get_temp(1))

    def save_temp(self, event_date, idSonde):
        """
        :param event_date:
        :param temp:
        :return:
        """
        print time.strftime("%a, %d %b %Y %H:%M:%S +0000", event_date) + " " + str(self.sonde[idSonde])

    def change_mode(self):
        """
        change le mode d'affichage, utilisé en tant que callback sur l appui d'un bouton
        :return:
        """
        if self.mode == 'dual_temp':
            self.mode = 'standard'
        else:
            self.mode = "dual_mode"

    def get_temp(self, idSonde):
        """
        getter pour les temperatures
        :param idSonde:
        :return:
        """
        return self.sonde[idSonde]
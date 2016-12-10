# -*- coding: utf-8 -*-


class Thermometre:
    def __init__(self):
        """
        :return:
        """
        self.mode = "dual"

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
        return text

    def create_temp_text(self, temperatures):
        """
        retourne les températures sur plusieurs lignes
        :param temps:
        :return:
        """
        text = "Ext. : {2.1f}\nInt. : {2.1f}".format(self.sonde[1], self.sonde[2])
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
        if self.mode ==' standard':
            return self.create_therm_text(self, self.sonde[idSondeRef], temp_consigne, mode, status)
        elif thermometre.mode == 'dual_mode':
            return self.create_temp_text(self, (self.sonde[1], self.sonde[2]))
        else:
            return "Mode d'affichage non configure"

    def read_temp(self, sondes):
        """
        set les semperatures
        :param sondes:
        :return:
        """
        self.sonde[1] = sondes.get_temp(1)
        self.sonde[2] = sondes.get_temp(2)

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
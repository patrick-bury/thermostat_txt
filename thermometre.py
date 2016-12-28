# -*- coding: utf-8 -*-
import time


class Thermometre:
    def __init__(self, config):
        """
        :return:
        """
        self.config = config
        self.sonde = {}
        self.step = 0
        self.mode_affichage = "dual"

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

    def create_temp_text(self):
        """
        retourne les températures sur plusieurs lignes
        :return:
        """
        line1 = "Ext. : {:2.1f}".format(self.sonde['ext'])
        if self.step%2 == 0:
            dot = " ."
        else :
            dot = ""
        line2 = "Int. : {:2.1f}".format(self.sonde['bureau'])
        text = line1 + dot + "\n" + line2
        return text

    def create_text(self, sonde_lieu, temp_consigne, confort_level, status, mode=None):
        """
        cree le texte a afficher en fonction du mode
        :param sonde_lieu:
        :param temp_consigne:
        :param mode:
        :param status:
        :return:
        """
        if mode is None:
            mode = self.mode_affichage
        self.step += 1
        if mode == 'dual':
            return self.create_temp_text()
        else:
            return self.create_therm_text(self.sonde[sonde_lieu], temp_consigne, confort_level, status)

    def read_temp(self, sondes):
        """
        set les semperatures
        :param sondes:
        :return:
        """
        for lieu in self.config.sondes.keys():
            read = sondes.read_temp(lieu)
            if read:
                self.sonde[lieu] = read

    def save_temp(self, event_date, lieu):
        """
        sauve les temperatures d'un lieu
        :param event_date:
        :param lieu:
        :return:
        """
        file_name = self.config.data_dir+lieu+".dat"
        print(file_name)
        fh = open(file_name, 'a')
        fh.write(time.strftime("%a, %d %b %Y %H:%M:%S +0000", event_date) + " " + str(self.sonde[lieu])+"\n")
        fh.close()

    def save_all_temps(self,now):
        """
        sauve toutes les temperatures dans le dossier data
        :param now:
        :return:
        """
        for lieu in self.config.sondes.keys():
            self.save_temp(now,lieu)

    def change_mode(self, channel):
        """
        change le mode d'affichage, utilisé en tant que callback sur l appui d'un bouton
        ;param channel canal utilisé
        :return:
        """
        print "changement mode affichage"
        if self.mode_affichage == 'dual':
            self.mode_affichage = 'standard'
        else:
            self.mode_affichage = "dual"

    def set_mode(self, mode_affichage):
        """
        setter pour le mode d'affichage
        :param mode:
        :return:
        """
        self.mode_affichage = mode_affichage

    def get_temp(self, lieu):
        """
        getter pour les temperatures
        :param idSonde:
        :return:
        """
        return self.sonde[lieu]

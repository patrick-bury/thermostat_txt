# -*- coding: utf-8 -*-
import re
import os


class DS1820:

    def __init__(self, config):
        """
        constructeur
        :param fileRoot:
        :param capteurs:
        :return:
        """
        self.fileRoot = config.sonde_file
        self.capteurs = config.sondes


    def read_temp(self, emplacement_capteur):
        """
        lit la temperature sur la capteur id_capteur
        :param id_capteur:
        :return:
        """
        filename = self.fileRoot+self.capteurs[emplacement_capteur]+"/w1_slave"
        if os.path.isfile(filename):
            ds1820_file = open(filename, "r")
            ds1820_file.readline()
            line2 = ds1820_file.readline().strip()
            m = re.findall(r"t=([\d]{1,5})", line2)
            temp = float(m[0])
            ds1820_file.close()
            return temp/1000
        else:
            return None
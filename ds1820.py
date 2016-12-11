# -*- coding: utf-8 -*-
import re


class DS1820:

    def __init__(self, fileRoot, capteurs):
        """
        constructeur
        :param fileRoot:
        :param capteurs:
        :return:
        """
        self.fileRoot = fileRoot
        self.capteurs = capteurs


    def get_temp(self, id_capteur):
        """
        lit la temperature sur la capteur id_capteur
        :param id_capteur:
        :return:
        """
        ds1820_file = open(self.fileRoot+self.capteurs[id_capteur]+"/w1_slave", "r")
        ds1820_file.readline()
        line2 = ds1820_file.readline().strip()
        m = re.findall(r"t=([\d]{1,5})", line2)
        temp = float(m[0])
        ds1820_file.close()
        return temp/1000

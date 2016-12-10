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
        file1 = open(self.fileRoot+self.capteurs[id_capteur]+"/w1_slave", "r")
        file1.readline()
        line2 = file1.readline().strip()
        m = re.findall(r"t=([\d]{5})", line2)
        temp = float(m[0])
        file1.close()
        return temp/1000

import re


class DS1820:

    def __init__(self, capteur1_id=False, capteur2_id=False):
        self.FILE_ROOT = "/sys/bus/w1/devices/"
        self.CAPTEUR1 = "28-011561577dff"
        self.CAPTEUR2 = "28-0115615a35ff"
        if capteur1_id:
            self.capteur1 = capteur1_id
        else:
            self.capteur1 = self.CAPTEUR1
        if capteur2_id:
            self.capteur2 = capteur2_id
        else:
            self.capteur2 = self.CAPTEUR2

    def get_temp(self,id_capteur):
        file1 = open(self.FILE_ROOT+self.capteur+str(id_capteur)+"/w1_slave", "r")
        file1.readline()
        line2 = file1.readline().strip()
        m = re.findall(r"t=([\d]{5})", line2)
        temp = float(m[0])
        file1.close()
        return temp/1000

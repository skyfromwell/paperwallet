from Adafruit_Thermal import *

class thermal_printer:
    def __init__(self):
        self.printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)
        
    def printImg(self, img, priv_key):
        self.printer.feed(3)
        self.printer.printImage(img)
        # I have some reservation about how to deal with encrypted private key, but need to wait for thermal_printer to look into it.
        if len(priv_key) <= 51:
            self.printer.printChar(priv_key[:17]+"\n")
            self.printer.justify("R")
            self.printer.printChar(priv_key[17:34]+"\n")
            self.printer.justify("L")
            self.printer.printChar(priv_key[34:]+"\m")
        else:
            self.printer.println(priv_key)

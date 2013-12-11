import config
import utility
import encryption
import drawImage
from subprocess import Popen, PIPE

class Wallet(object): 
    def __init__(self):
        self.image_file_name = None
        self.thermal_print = None
        self.encrypt_priv_key = False
        self.pub_key = None
        self.priv_key = None
        self.is_keys_good = False
           
    def __getConfig(self):
        self.image_file_name, self.thermal_print, self.encrypt_priv_key = utility.configHandler().getConfig()
        
    def __genKeys(self):
        try:
            process = Popen(config.cmd[self.cointype], stdout=PIPE)
        except:
            process = Popen(config.cmd['bitcoin'], stdout=PIPE)
        addrs = process.stdout.read().split()
        if len(addrs[3]) >= 27 and len(addrs[5]) == 51:
            self.is_keys_good = True
            self.pub_key = addrs[3]
            if self.encrypt_priv_key:
                self.priv_key = encryption.encode_pw(addrs[5], self.encrypt_priv_key)
            else:
                self.priv_key = addrs[5]
            
            if len(self.priv_key)<= 51:
                self.image_file_name += '-blank.bmp'
            else:
                self.image_file_name += '-enc.bmp'
    
    def getPaperWallet(self):
        if self.image_file_name is None:
            self.__getFileName()
        if self.pub_key is None and self.priv_key is None:
            self.__genKeys()
        if self.is_keys_good:
            drawImage.drawImage(config.home_path+self.image_file_name, self.thermal_print).drawImage(self.pub_key, self.priv_key)
            

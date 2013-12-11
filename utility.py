import sqlite3
import config
import sys

sql_get_comm = "SELECT cointype FROM settings LIMIT 1;"
sql_reset_comm = "UPDATE settings SET cointype='bitcoin';"
DEFAULTCOIN = 'bitcoin'

class configHandler:
    def __init__(self):
        self.img_file_name = ""
        self.thermal_print = 0
        self.encryption = ""
        self.conn = None
        self.cur = None
        try:
            self.conn = sqlite3.connect(config.db_path)
            self.cur = self.conn.cursor()
            self.cur.execute(sql_get_comm)
            coin_type, self.thermal_print, self.encryption = self.cur.fetchone()
            if not coin_type:
                coin_type = DEFAULTCOIN
            if self.encryption:
                coin_type += '-enc'
            self.img_file_name = config.image_name[coin_type]
        except sqlite3.Error, e:
            print 'Error %s:' % e.args[0]
            sys.exit()
    
    def getConfig(self):
    
        return (self.img_file_name, self.thermal_print, self.encryption)
    
    def reset(self):
        self.cur.excute(sql_reset_comm)
        self.conn.commit()
        
    def close(self):
        self.conn.close()
    

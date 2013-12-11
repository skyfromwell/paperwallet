#to do next: didn't specify font, need to see how thermal_printer result. Also there is some improvement area in add text.
# one change -- if you have thermal_printer with it, print it, otherwise saving a bmp file.
import os
import Image
import ImageDraw
import getQrCode
from config import home_path
import thermal_print

LINEWIDTH = 17
LINEHEIGHT = 23
STARTPOS = 110
CHARDISTANCE = 15

class drawImage:
    
    def __init__(self, img_name, thermal_print):
        self.img = Image.open(img_name)
        self.thermal_print = thermal_print
        
    def drawImage(self, pub_key, priv_key):
        self.__add_text(pub_key, 38)
        self.__getQrImage(pub_key, (175,175), (150, 106))
        self.__getQrImage(priv_key, (220,220), (125,560))
        self.__add_text(priv_key, 807)
        if self.thermal_print:
            thermal_print.thermal_printer().printImg(self.img, priv_key)
        else:
            self.img.save(home_path+'new.bmp')
        
        
    def __getQrImage(self, key, size, pos):
        qr_img = getQrCode.getQrCode(key).resize(size, Image.NEAREST)
        self.img.paste(qr_img, pos)
        
    def __add_text(self, key, pos):
        draw = ImageDraw.Draw(self.img)
        key_length=len(key)
        while (key_length % LINEWIDTH):
            key += " "
            key_length = len(key)
        for x in range(key_length/LINEWIDTH):
            last_char_pos = 0
            for y in range(LINEWIDTH):
                char = key[(x*LINEWIDTH)+y]
                char_size = draw.textsize(char)
                if y:
                    draw.text((STARTPOS, pos+(x*LINEHEIGHT)), char)
                    last_char_pos = STARTPOS+char_size[0]+(CHARDISTANCE-char_size[0])
                else:
                    draw.text((last_char_pos, pos+(x*LINEHEIGHT)), char)
                    last_char_pos = last_char_pos+char_size[0]+(CHARDISTANCE-char_size[0])
                    

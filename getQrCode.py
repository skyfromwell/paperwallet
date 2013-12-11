import qrcode

def getQrCode(key):
    qr = arcode.QRCode(box_size=10)
    qr.add_data(key)
    qr.make()
    
    return qr.make_image()

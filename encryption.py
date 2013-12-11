#remove all others only keep Bip38 here. Need to learn more about this.

from bitcoin.bip38 import Bip38
from bitcoin.key import CKey
from bitcoin.base58 import CBase58Data

__b58chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
__b58base = len(__b58chars)


def encode_pw(key, pw):
    key = CKey()
    decode_string = __decode_b58(key)[1:-4]
    key.generate(decode_string)
    key.set_compressed(False)
    bt = Bip38(key, pw)
    
    return str(CBase58Data(bt.get_encrypted(), 0x01))

def __encode_b58(v):
    value = 0L
    for (i, c) in enumerate(v[::-1]):
        value += (256**i) * ord(c)
    result = ""
    while value >= __b58base:
        div, mod = divmod(value, __b58base)
        result = __b58chars[mod] + result
        value = div
    result = __b58chars[value] + result
    pad = 0
    for c in v:
        if c=='\0':
            pad += 1
        else:
            break
    
    return (__b58chars[0]*pad) + result
    
    
def __decode_b58(v):
    value = 0L
    for (i, c) in enumerate(v[::-1]):
        value += __b58chars.find(c) * (__b58base**i)
    result = ""
    while value >= 256:
        div, mod = divmod(value, 256)
        result = chr(mod) + result
        value = div
    result = chr(value) + result
    pad = 0
    for c in v:
        if c==__b58chars[0]:
            pad += 1
        else:
            break
    result = chr(0)*pad + result
    
    return result

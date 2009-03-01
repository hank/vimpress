import sys
from itertools import izip, cycle
def xor_crypt_string(data, key):
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))

if len(sys.argv) < 2:
  print "Supply a password."
  exit(0)

print "Your XORed Password: '"+xor_crypt_string(sys.argv[1], 'seed123').encode("string-escape")+"'"

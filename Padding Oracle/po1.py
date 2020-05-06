from M2Crypto import EVP
import os

# sample key.  Your attack should not rely on this (or any) key
# but instead rely on calls to dec_check
key = "E\xdd\xf85\x7fL\x19\x97\xa4(\xc6\xc1\xf8$\xb1\xd9"

def dec_check(c):
	iv = c[:16]
	ctxt = c[16:]
	cobj = EVP.Cipher('aes_128_cbc', key, iv, 0, 0)
	ptxt = ''
	ptxt = cobj.update(ctxt)
	ptxt += cobj.final()
	return ''

def enc(m):
	iv = os.urandom(16)
	cobj = EVP.Cipher('aes_128_cbc', key, iv, 1, 0)
	c = cobj.update(m)
	c += cobj.final()
	return iv+c



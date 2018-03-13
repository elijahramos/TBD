from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os # some of this needs the OS's PRNG
import cnsts

def norm(y, key): # use CBC (AES), also the Key has to be less than 32bytes long (256bit), also the message is a byte string.
	if(len(y)%cnsts.IVLengthExpt!=0):
		raise Exception("byte count has gotta be a multiple of 16")
		# I may wana go back and add some kind of padding thingy,
	
	padder = padding.PKCS7(cnsts.padding).padder()
	padded_data = padder.update(y)
	padded_data += padder.finalize()
	
	if(len(key)<cnsts.keyLengthExpt): raise Exception("key's gotta be AT LEAST 32 bytes")
	backend = default_backend()
	IV = os.urandom(cnsts.IVLength)
	cipher = Cipher(algorithms.AES(key), modes.CBC(IV), backend=backend)
	encryptor = cipher.encryptor()
	C = encryptor.update(padded_data) + encryptor.finalize()
	return [C,IV]

def inv(C,IV,key):
	backend = default_backend()
	cipher = Cipher(algorithms.AES(key), modes.CBC(IV), backend=backend)
	decryptor = cipher.decryptor()
	dun = decryptor.update(C) + decryptor.finalize()
	
	unpadder = padding.PKCS7(cnsts.padding).unpadder()
	data = unpadder.update(dun)
	
	return (data + unpadder.finalize())

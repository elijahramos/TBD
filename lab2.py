# so a quick thing to know here b4 we get into this heavly is that you can have byte strings, basically its an array of values between 0 and 255
# similar to how you can take a file and put it in the program as a big string A-la open("file.txt").read()
# you can do the same thing but return it as a byte string by adding "rb" as a parameter
# the command below will copy the file "this" to "that"
# open("that","wb").write(open("this","rb").read())
# to convert a string into bytes use bytes("sampleTxt","utf-8")

# the reccomended cryptography suite for python3, 
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os # some of this needs the OS's PRNG

#class epicFail(Exception): pass

class Constants():# constants dont exist in python3, 
	def __init__(self):
		self.keyLength=32
		self.IVLength=16
		self.keyLengthExpt=32
		self.IVLengthExpt=16
		self.padding=128 #TODO: solve the padding issue

def main():
	s = b'1234123412341234'
	k = os.urandom(cnst.keyLength)# Constant#1 is the key length
	g = Myencrypt(s,k)
	print(g)
	f = inverseMyencrypt(g[0],g[1],k)
	print(f)

def Myencrypt(y, key): # use CBC (AES), also the Key has to be less than 32bytes long (256bit), also the message is a byte string.
	if(len(y)%cnst.IVLengthExpt!=0):
		raise Exception("byte count has gotta be a multiple of 16")
		# I may wana go back and add some kind of padding thingy,
	
	padder = padding.PKCS7(cnst.padding).padder()
	padded_data = padder.update(y)
	padded_data += padder.finalize()
	
	if(len(key)<cnst.keyLengthExpt): raise Exception("key's gotta be AT LEAST 32 bytes")
	backend = default_backend()
	IV = os.urandom(cnst.IVLength)
	cipher = Cipher(algorithms.AES(key), modes.CBC(IV), backend=backend)
	encryptor = cipher.encryptor()
	C = encryptor.update(padded_data) + encryptor.finalize()
	return [C,IV]

def inverseMyencrypt(C,IV,key):
	backend = default_backend()
	cipher = Cipher(algorithms.AES(key), modes.CBC(IV), backend=backend)
	decryptor = cipher.decryptor()
	dun = decryptor.update(C) + decryptor.finalize()
	
	unpadder = padding.PKCS7(cnst.padding).unpadder()
	data = unpadder.update(dun)
	
	return (data + unpadder.finalize())

def MyfileEncrypt(filepath):
	return [0,0,0,0]#(C, IV, key, ext)

def inverseMyfileEncrypt(C,IV,key,ext):
	return ("")#it would just write to the same file

def MyRSAEncrypt(filepath, RSA_Publickey_filepath):
	return [0,0,0,0]#(RSACipher, C, IV, ext)

cnst=Constants()
main()

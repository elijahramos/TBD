# Cryptology module imports
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

def norm(key,keyPath): # this will work independent of MyfileEncrypt
	publicKeyData = open(keyPath,"rb").read()
	k = serialization.load_pem_public_key(publicKeyData,backend=default_backend())# load public key 
	RSAC = k.encrypt(key,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))# do the encryption
	return RSAC # returns the encrypted key
def inv(RSAC,keyPath):
	kData = open(keyPath,"rb").read()
	k = serialization.load_pem_private_key(kData,password=None,backend=default_backend())
	d = k.decrypt(RSAC,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
	return d # the deciphered key

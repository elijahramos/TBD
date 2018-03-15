# Cryptology module imports
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

import MyfileEncrypt

def norm(plainText,publicKeyData):
	g=MyfileEncrypt.norm(plainText)# passthrough
	k = serialization.load_pem_public_key(publicKeyData,backend=default_backend())# load public key 
	RSAC = k.encrypt(g[2],padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))# do the encryption
	return [RSAC,g[0],g[1]]# [RSAC,C,IV]
def inv(RSAC,C,IV,kData):
	k = serialization.load_pem_private_key(kData,password=None,backend=default_backend())
	d = k.decrypt(RSAC,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
	return MyfileEncrypt.inv(C,IV,d) # the deciphered data

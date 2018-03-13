# Cryptology module imports
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

import MyfileEncrypt

def norm(filePath,publicKeyPath):
	g=MyfileEncrypt.norm(filePath)# passthrough
	
	k = serialization.load_pem_public_key(open(publicKeyPath, "rb").read(),backend=default_backend())# load public key 
	c = k.encrypt(m,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))# do the encryption
	#write 'c' to file.
	return [c,g[0],g[1],g[3]]# [RSAC,C,IV,ext]
def inv(RSAC,filePath,IV,ext,kPath):
	k = serialization.load_pem_private_key(open(kPath, "rb").read(),password=None,backend=default_backend())
	d = k.decrypt(RSAC,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
	return MyfileEncrypt.inv(filePath,IV,d,ext) # the deciphered data

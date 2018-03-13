# Cryptology module imports
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

import MyfileEncrypt

def norm(filePath,publicKeyPath):
	g=myfileEncrypt(filePath)
	
	k = #public key obj, Im looking for a way to turn plain text public keyis in something this uses.
	c = k.encrypt(m,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
	#write to file.
	return [c,g[0],g[1],g[3]]
def inv(RSAC,C,IV,ext,kPath):
	k = serialization.load_pem_private_key(open(kPath, "rb").read(),password=None,backend=default_backend())
	d = k.decrypt(RSAC,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
	# also write to file
	return d # the deciphered data

import MyfileEncrypt

def norm(filePath,publicKeyPath):
	g=myfileEncrypt(filePath)
	
	#TODO: encrypt the key with RSA and OAEP padding.
	# the result goes in slot #0
	
	
	
	return [0,g[0],g[1],g[3]]
def inv(RSAC,C,IV,filePath):
	
	#TODO: decryption loal
	
	return 0 # the deciphered data

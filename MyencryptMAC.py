# these are the cryptography suites, they handle most of the magics
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
#HMAC, for your health
from cryptography.hazmat.primitives import hashes, hmac

import os # some of this needs the OS's PRNG
import cnsts # Constants! for your health.

# uses CBC (AES), also the Key has to be less than 32bytes long (256bit), also the message is a byte string. not to be confused with regular strings.
def norm(y, key, mKey):#forgive my unclear variables, but y is the Plain text variable. this was ported from a monolithic version of the program.
	# also key is simply a regular key
	# the mKey is the HMAC key.
	
	#this is the padder, it makes the plain txt kosher for the encryption algo.
	padder = padding.PKCS7(cnsts.padding).padder()# makes the padding obj
	padded_data = padder.update(y)# an update of sorts
	padded_data += padder.finalize()# puts some padding data on the plain txt
	
	# exception is self explanitory, well Expt is short for exponent
	if(len(key)<cnsts.keyLengthExpt): raise Exception("key's gotta be AT LEAST 32 bytes")
	
	backend = default_backend()# this is required a few lines down, dono what it does Im just the code kobold
	
	IV = os.urandom(cnsts.IVLength)# gather only the FINEST RNG for our purposes.
	cipher = Cipher(algorithms.AES(key), modes.CBC(IV), backend=backend)# makes the encryption algo.
	encryptor = cipher.encryptor()# and then the encryptor
	C = encryptor.update(padded_data) + encryptor.finalize() # then we bake the cipher txt.
	
	#we encrypted, now we MAC. er, setup the mac thingy.
	mac = hmac.HMAC(mKey, hashes.SHA256(), backend=default_backend())
	mac.update(C) # put the cypher txt in the HMAC
	
	# the HMAC is finalized in the return statement
	return [C,IV,mac.finalize()]# puts the cipher txt, IV value, and the tag in a 3 slot array list, this is for manipulation outside the function.

def inv(C,IV,key,tag,mKey):# basically, the decryption thingy.
	
	# a verification step
	mac = hmac.HMAC(mKey, hashes.SHA256(), backend=default_backend())
	mac.update(C) # put the cypher txt in the HMAC
	try: mac.verify(tag) # try to verify this.
	except: return None # a verification failure raises an exception. I'd probably flesh this out a bit more had I had the time.
	
	backend = default_backend()# again with the backend
	cipher = Cipher(algorithms.AES(key), modes.CBC(IV), backend=backend)# we have to REBUILD the same algo.
	decryptor = cipher.decryptor()# you know the drill.
	dun = decryptor.update(C) + decryptor.finalize()# decrypt that stuff
	
	#but wait, we also have to remove the padding.
	unpadder = padding.PKCS7(cnsts.padding).unpadder()# make the unpadder, Uh-gain.
	data = unpadder.update(dun)# removin...
	
	return (data + unpadder.finalize())# now we have our text, in all of its plain glory.

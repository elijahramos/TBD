# so a quick thing to know here b4 we get into this heavly is that you can have byte strings, basically its an array of values between 0 and 255
# similar to how you can take a file and put it in the program as a big string A-la open("file.txt").read()
# you can do the same thing but return it as a byte string by adding "rb" as a parameter
# the command below will copy the file "this" to "that"
# open("that","wb").write(open("this","rb").read())
# to convert a string into bytes use bytes("sampleTxt","utf-8")

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

import os
import cnsts
import Myencrypt

# so this was me testing RSA encryption using both a key generator and a .pem key I had left over from the first lab.
kg = rsa.generate_private_key(public_exponent=65537,key_size=2048,backend=default_backend())
k = serialization.load_pem_private_key(open("/home/snerfoil/.ssh/TBD-secret2.pem", "rb").read(),password=None,backend=default_backend())
ppk = serialization.load_pem_public_key(open("/home/snerfoil/.ssh/TBD-secret2.pub", "rb").read(),backend=default_backend())

m = b'I like butts :3'
c = ppk.encrypt(m,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
d = k.decrypt(c,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
print(m)
print(c)
print(d)


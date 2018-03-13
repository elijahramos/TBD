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
import MyRSAEncrypt
def main():
	runTiem = True
	while(runTiem):
		print("0: exit\n1: encrypt\n2: decrypt\n3: makekeys\n--> ",end='')
		u = input()
		if(u=='0'): runTiem=False
		elif(u=='1'): option1()
		elif(u=='2'): option2()
		elif(u=='3'): option3()

def option1():
	print("Select file to encrypt: ",end='')
	filePath = input()
	print("Select public key: ",end='')
	keyPath = input()
	g = MyRSAEncrypt.norm(filePath,keyPath)# [RSAC,filePath,IV,".enc"]
	
	open((filePath+".rsa"), "wb").write(g[0])
	open((filePath+".iv"), "wb").write(g[2])
	open((filePath),"wb").write(b'\0')
	
	print("done",end='')
	input()
	
def option2():
	print("Select file to encrypt: ",end='')
	filePath = input()
	print("Select private key: ",end='')
	keyPath = input()
	
	rsa = open((filePath+".rsa"),"rb").read()
	iv = open((filePath+".iv"),"rb").read()
	
	open((filePath),"wb").write(MyRSAEncrypt.inv(rsa,filePath,iv,".enc",keyPath))
	
	print("done",end='')
	input()
	
def option3():
	print("where do you wish to save the keys?(dont type ext, just filename): ",end='')
	u = input()
	kg = rsa.generate_private_key(public_exponent=65537,key_size=2048,backend=default_backend())
	#pk = private_key.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.PKCS8,encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword'))
	prvkNoENC = kg.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.PKCS8,encryption_algorithm=serialization.NoEncryption())
	pubkNoENC = kg.public_key().public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)
	
	open(u+".pem","wb").write(prvkNoENC)
	open(u+".pub","wb").write(pubkNoENC)
	print("done",end='')
	input()

main()


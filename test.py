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
import MyfileEncrypt
import Myencrypt
import pickle   #use pickle as opposed to JSON due to issues with byte strings
                #pickle.dumps(theThingYouWantToBecomeAByteString) returns a byte string.
                #pickle.loads(byteString) will do the inverse of that.

def main():
	runTiem = True
	while(runTiem):
		print("0: exit\n1: encrypt\n2: decrypt\n3: makekeys\n4: basicEncrypt\n5: basicDecrypt\n--> ",end='')
		u = input()
		if(u=='0'): runTime=False
		elif(u=='1'): option1()
		elif(u=='2'): option2()
		elif(u=='3'): option3()
		elif(u=='4'): option4()
		elif(u=='5'): option5()

def option1():
	print("Select file to encrypt: ",end='')
	filePath = input()
	print("Select public key: ",end='')
	keyPath = input()
	
	f = MyfileEncrypt.norm(filePath) #filepath = [C, IV, key,fileDir,fileName,fileExt]
	g = MyRSAEncrypt.norm(f[2],keyPath) #encrypted key
	
	open((f[3]+f[4]+".ukn"),"wb").write(pickle.dumps([g,f[0],f[1],f[5]])) #[RSAC,C,IV,fileext]
	os.remove(filePath) #delete the file.
	
	print("done",end='')
	input()
	
def option2():
	print("Select file to decrypt: ",end='')
	filePath = input()
	print("Select private key: ",end='')
	keyPath = input()
	
	fileObj = open(filePath, "rb") #open file, and save the referance for later
	location = filePath.rstrip(os.path.basename(fileObj.name)) #cut off the file's directory
	cutFile = (os.path.basename(fileObj.name)).partition('.') #place the file's name into a list [fileName, ., ext]
	fileString = fileObj.read()
	
	g = pickle.loads(fileString) #gets the above [RSAC, C, IV, ext]
	
	buff = Myencrypt.inv(g[1],g[2],MyRSAEncrypt.inv(g[0],keyPath))
	#we would use MyfileEncrypt if JUST the cipher text was stored in a file
	#but it isnt, its pickled with the IV, RSAC, and ext for convienence.
	open((cutFile[0]+'.'+g[3]),"wb").write(buff)
	os.remove(filePath) # delete the file.
	
	print("done",end='')
	input()
	
def option3(): #key generator
	print("where do you wish to save the keys?(dont type ext, just filename): ",end='')
	u = input()
	kg = rsa.generate_private_key(public_exponent=65537,key_size=2048,backend=default_backend())
	#pk = private_key.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.PKCS8,encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword'))
	prvkNoENC = kg.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.PKCS8,encryption_algorithm=serialization.NoEncryption())
	pubkNoENC = kg.public_key().public_bytes(encoding=serialization.Encoding.PEM,format=serialization.PublicFormat.SubjectPublicKeyInfo)
	
	open(u+"_prv.pem","wb").write(prvkNoENC)
	open(u+"_pub.pem","wb").write(pubkNoENC)# these are both .pem files, I looked it up.
	print("done",end='')
	input()
	
def option4():
	print("select file to encrypt: ",end='')
	filePath = input();
	g = MyfileEncrypt.norm(filePath) # [C, IV, key,fileDir,fileName,fileExt]
	
	open((g[3]+g[4]+".bukn"),"wb").write(pickle.dumps([g[0],g[1],g[5]]))# [C,IV,ext]
	open((g[3]+g[4]+".buknk"),"wb").write(g[2])# key RAWR
	os.remove(filePath) # delete the file.
	
	print("done",end='')
	input()
	
def option5():
	print("select file to decrypt: ",end='')
	filePath = input()
	print("specify the file's key: ",end='')
	keyPath = input()
	
	cutt = (os.path.basename(filePath)).partition('.') # we cutout the file's name and ext
	
	g = MyfileEncrypt.inv(filePath,keyPath) # [P,ext]
	
	open((cutt[0]+"."+g[1]),"wb").write(g[0])# dere it is
	os.remove(filePath) # delete the file.
	os.remove(keyPath) # delete the file.
	print("done",end='')
	input()

main()


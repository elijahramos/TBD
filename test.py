# so a quick thing to know here b4 we get into this heavly is that you can have byte strings, basically its an array of values between 0 and 255
# similar to how you can take a file and put it in the program as a big string A-la open("file.txt").read()
# you can do the same thing but return it as a byte string by adding "rb" as a parameter
# the command below will copy the file "this" to "that"
# open("that","wb").write(open("this","rb").read())
# to convert a string into bytes use bytes("sampleTxt","utf-8")

import os
import cnsts
import Myencrypt

# prototype myfiledecrypt.norm
print("specify filename: ",end='')
a = input()
s = open(a,"rb").read()
k = os.urandom(cnsts.keyLength)# Constant#1 is the key length
g = Myencrypt.norm(s,k) # 0:C 1:IV
#open((a+".fucc"),"wb").write(g[0])
#open((a+".iv"),"wb").write(g[1])
#open((a+".key"),"wb").write(k)
#print("done")

# prototype myfiledecrypt.inv
#print("specify filename: ",end='')
#a = input()
#b = open((a+".fucc"),"rb").read()
#c = open((a+".iv"),"rb").read()
#d = open((a+".key"),"rb").read()
#f = Myencrypt.inv(b,c,d)
#open(a,"wb").write(f)
#print("done")


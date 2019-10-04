import hashlib
from base64 import b64encode, b64decode
from simplecrypt import encrypt, decrypt


def strongcrypt(masterpass,cryptme):
 ciphertext = encrypt(masterpass,cryptme)
 b64cipher=b64encode(ciphertext)
 return(b64cipher)

def strongdecrypt(masterpass,decryptme):
 bytecipher=b64decode(decryptme)
 return(decrypt(masterpass, bytecipher))
 
def hashthis(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def inputs(mode):
 global imail,isite,ipass,imaster
 print("input mail adress")
 imail=input()
 print("input site name")
 isite=input()
 if mode=="s":
  print("input password")
  ipass=input()
 print("input masterpass")
 imaster=input()

def storepass(mail,site,password,masterpass):
 f=open("kasa",'r')
 contents=f.read()
 f.close()
 if contents.find(hashthis(mail))>-1:  #burda site mail ortak bak
  if contents.find(hashthis(site))>-1: 
   print("mail and site already exists")
   return -1
 f= open("kasa","a+")
 f.write(hashthis(mail) +"\n" + hashthis(site) + "\n")
 cryptedpass=strongcrypt(masterpass,password)
 f.write(cryptedpass.decode("utf-8") + "\n" +"\n")
 f.close

f=open("kasa","a") #creates file if not exist and closes
f.close()
print("select mode, s for store, d for decrypt")
mode=input()

if mode=="s":
 inputs("s")
 print("please wait")
 storepass(imail,isite,ipass,imaster)
 print("Done")

if mode=="d":
 inputs("d")
 hashedmail=hashthis(imail)
 hashedsite=hashthis(isite)
 f=open("kasa","r")
 contents=f.read()
 f.close
 searchthing=hashedmail+"\n"+hashedsite+"\n"
 first_index_login=contents.find(searchthing)
 if first_index_login == -1:
  print("cant find username and site")
  exit()
 last_index_login=first_index_login+len(searchthing) #+1
 last_index_password=contents.find("\n",last_index_login)
 cryptedpass= contents[last_index_login:last_index_password]
 print("please wait")
 decryptedpass=strongdecrypt(imaster,cryptedpass)
 print(decryptedpass)


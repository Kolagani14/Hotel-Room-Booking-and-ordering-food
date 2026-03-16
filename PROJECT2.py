#Encrypted Chat For Indian Army
import random
import string

#For encryption messesges taking the digits and Puncutation and alphabets
passcodes=" "+string.punctuation + string.digits + string.ascii_letters

#In string data type there is no copy method, So we have to covert to list
passcodes=list(passcodes)

#In passcodes the list is stored, Thats why its accepted
key= passcodes.copy()

#Here shuffle is using for to build strong code 
random.shuffle(key)
#print("passcodes : ", passcodes)
#print("key : ", key)

#Encryption chat
Text = input("Enter the message : ")
Encrypt_Message = " "

#Here index is start with 0 in passcodes until end with some another number
#In the passcodes of every index has been going to checking through the letter
#Because of iteration 
for letter in Text:
    index = passcodes.index(letter)

#At the same time key of index is equal to index of letters
    Encrypt_Message += key[index]
print("Original  message : ", Text)
print("Encrypted message : ", Encrypt_Message)

#Dencrypt Message
Encrypt_Message = input("Enter the encrypted message : ")
Dencrypt_Message= " "

#Encrypted message is going to be dencrypted
for letter in Encrypt_Message:
    index = key.index(letter)
    Dencrypt_Message += passcodes[index]

print("Encrypted message : ", Encrypt_Message)
print("Dencrypted message : ", Dencrypt_Message)


#For understanding purpose i wrote a little program 
#a=["a","b","c","d"]
#b=["1","2","3","4"]
#text=input("enter :")
#write=" "
#for i in text: #bc
#    index=a.index(i)
#    write=write+b[index]#""+b[1]=2
#print(text)
#print(write)
    




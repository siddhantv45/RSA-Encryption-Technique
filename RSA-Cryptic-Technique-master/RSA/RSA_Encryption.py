import RSA_Functions

# Taking prime numbers as input from the user
print("Input two prime numbers with a space in between")
inputt=input()
P1,P2=inputt.split()
P1,P2=int(P1),int(P2)

#List of possible keys
possible_keys=RSA_Functions.public_key(P1,P2)
print(possible_keys)
key_select=int(input("Which key do you want to use?"))		#Giving the user option to select their key

print("You have selected",key_select,P1*P2,"as your public key")

#Reading the sample file
a=open("sample.txt","r")
a=a.read()
RSA_Functions.plaintext(a)
b=open("data_wordsonly.txt","r")
b=b.read()
RSA_Functions.cipher_encrypt(b,key_select,P1,P2)

print("Success")
print("Your data has been encrypted using this key")
print("Exported to data_encrypted.txt")
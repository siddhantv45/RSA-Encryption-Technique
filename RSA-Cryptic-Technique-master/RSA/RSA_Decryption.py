import RSA_Functions

print("RSA Decryption Portal")
print("You will be provided a private key for your given public key")
print("Input two prime numbers and the public key you have respectively, seperated by a space")
a=input()
P1,P2,key_select=a.split()
P1,P2,key_select=int(P1),int(P2),int(key_select)

#List of Possible Keys
print("For the given public key, The following private Keys are available")
print(RSA_Functions.private_key(P1,P2,key_select))
key2_select=int(input("Which key do you want to use?"))		#Giving the user option to select their key

print("You have selected",key2_select,P1*P2,"as your private key")

#Reading the Encrypted File
b=open("data_encrypted.txt","r")
b=b.read()
RSA_Functions.plainify_encrypted(b,P1,P2,key2_select)

print("Success")
print("Your data has been decrypted")
print("Exported to data_decrypted.txt")


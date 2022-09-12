def plaintext(data):
	
	data=data.replace('\n',' ')
	data=data.lower()
	alpha='abcdefghijklmnopqrstuvwxyz '     #Elements that we want in our plaintext
	
	main_data=''            #A String that will contain only alphabets and spaces

	for i in range(len(data)):
		if(data[i] in alpha):
			main_data=main_data+str(data[i])
	
	export=[x for x in main_data.split()]
	f=open("data_wordsonly.txt","w")    #Exporting the plaintext


	for i in range(len(export)):
		f.write(export[i])
		f.write("\n")
		f.flush()
	
	return

# Using Euclid's Algorith to find GCD

def gcd(prime1,prime2):

	if(prime2>prime1):
		prime1,prime2=prime2,prime1

	while(prime2!=0):
		temp=prime1
		prime1=prime2
		prime2=temp%prime2
	
	return(prime1)

#Finding the key for encryption of the given data


def public_key(prime1,prime2):

	product=prime1*prime2

	#Finding how many numbers betwwen 1 and product are coprime with product
	coprime_numbers=(prime1-1)*(prime2-1)
	
	possible_keys=[]       #It will contain all the possible keys

	#Encryption Key must be between 1 and coprime_numbers
	#It must pe coprime with product and coprime_numbers
	
	k=0			#We have to set a counter as RSA takes large prime numbers
	for i in range(2,coprime_numbers):
	
		if(gcd(i,coprime_numbers)==1):
	
			if(gcd(i,product)==1):
			
				possible_keys.append(i)
				k+=1
				if(k==20):		#For the sake of simplicity we are giving only 20 possible encryption keys
					break
	
	return possible_keys

#This is the main coding algorithm

def alpha_shift(prime1,prime2,key,index):
	product=prime1*prime2
	new_index=(index**key)%product 	#This is RSA formula for encryption
	return new_index


def cipher_encrypt(plaindata,key_select,prime1,prime2):	#Takes as input a string in plaintext and encryptionkey
	
	final_encrypt=''	#This will contain final encrypted data
	plaindata=plaindata.replace('/n',' ')
	alphaa='abcdefghijklmnopqrstuvwxyz'
	
	for i in range(len(plaindata)):
		
		if(plaindata[i] in alphaa):
			d=alphaa.index(plaindata[i])
			d=alpha_shift(prime1,prime2,key_select,d)
			final_encrypt=final_encrypt+str(d)+','
		
		else:
			final_encrypt=final_encrypt+str(plaindata[i])
	
	l=[x for x in final_encrypt.split()]
	
	#Exporting encrypted data in a text file
	f=open("data_encrypted.txt","w")
	
	for i in range(len(l)):
		f.write(l[i])
		f.write("\n")
	f.flush()
	return


def private_key(prime1,prime2,encryption_key):
	coprime_numbers=(prime1-1)*(prime2-1)

	#Range has been set so as to remove the obvious wrong answers
	for i in range(coprime_numbers//encryption_key,coprime_numbers):
		temp=(encryption_key*i)%coprime_numbers
		if(temp==1):		#Breaking the function as this pattern repeats
			pivot=i
			break
	decryption_keys=[]		#This will contain possible decryption keys
	
	#Using the pattern to generate 20 more keys
	for i in range(20):
		decryption_keys.append(coprime_numbers*i+pivot)
	return decryption_keys

#This is main algorithm for decrypting
def decrypt_this(prime1,prime2,key,index):
	product=prime1*prime2
	index=int(index)
	new_index=(index**key)%product 	#This is RSA formula for decryption
	return new_index

def plainify_encrypted(encrypted_data,prime1,prime2,key2_select):
	alphaa='abcdefghijklmnopqrstuvwxyz'
	encrypted_data=encrypted_data.replace('\n',' ')
	decrypted_data=''
	temp=[x for x in encrypted_data.split()]
	for i in range(len(temp)):
		temp1=[x for x in temp[i].split(',')]
		temp1.pop(len(temp1)-1)
		for j in range(len(temp1)):
			new_index=decrypt_this(prime1,prime2,key2_select,temp1[j])
			decrypted_data=decrypted_data+str(alphaa[new_index])
		decrypted_data=decrypted_data+'\n'

	l=[x for x in decrypted_data.split()]
	
	#Exporting decrypted data in a text file
	f=open("data_decrypted.txt","w")
	
	for i in range(len(l)):
		f.write(l[i])
		f.write("\n")
	f.flush()
	return
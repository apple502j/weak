import crypto

keys=crypto.generateKeys()
publicKey=keys[0]
privateKey=keys[1]
print("Generate your key.")
print("PUBLIC:\n" + publicKey)
print("\nPRIVATE:\n"+privateKey)

encryptText=input("What should I encrypt? (using private key) >>>")
encrypted=crypto.crypt(encryptText,privateKey)
print(encrypted)
decrypted=crypto.crypt(encrypted,publicKey)
print(decrypted)

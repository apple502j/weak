import crypto

PUBLIC_KEY, PRIVATE_KEY = crypto.generateKeys()
print("Generated your key.")
print("PUBLIC:\n" + PUBLIC_KEY)
print("\nPRIVATE:\n" + PRIVATE_KEY)

_ = crypto.crypt(input("What should I encrypt? (using private key) >>> "),
                 PRIVATE_KEY)
print(_)
print(crypto.crypt(_, PUBLIC_KEY))

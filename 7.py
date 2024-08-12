import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# ASCII Header
ascii_header = """

  ____                   _                            
 |  _ \ _   _ _ __ _ __ | | ___                       
 | |_) | | | | '__| '_ \| |/ _ \                      
 |  __/| |_| | |  | |_) | |  __/                      
 |_|___ \__,_|_|  | .__/|_|\___|    _   _             
 | ____|_ __   ___|_|__ _   _ _ __ | |_(_) ___  _ __  
 |  _| | '_ \ / __| '__| | | | '_ \| __| |/ _ \| '_ \ 
 | |___| | | | (__| |  | |_| | |_) | |_| | (_) | | | |
 |_____|_| |_|\___|_|   \__, | .__/_\__|_|\___/|_| |_|
 |  \/  | ___  ___ ___  |___/|_| _(_)_ __   __ _      
 | |\/| |/ _ \/ __/ __|/ _` |/ _` | | '_ \ / _` |     
 | |  | |  __/\__ \__ \ (_| | (_| | | | | | (_| |     
 |_|  |_|\___||___/___/\__,_|\__, |_|_| |_|\__, |     
                             |___/         |___/                                                                                                                                     
"""
print(ascii_header)

# Generate RSA keys
key = RSA.generate(2048)
public_key = key.publickey()

# Show the user's public key (Base64 encoded)
public_key_pem = public_key.export_key()
public_key_base64 = base64.b64encode(public_key_pem).decode('utf-8')
print("Your RSA Public Key (Base64 Encoded):")
print(public_key_base64)

# Ask the user for the recipient's public key
recipient_public_key_base64 = input("\nEnter the recipient's RSA Public Key (Base64 Encoded): ")

# Decode the recipient's public key from Base64
recipient_public_key_pem = base64.b64decode(recipient_public_key_base64)
recipient_public_key = RSA.import_key(recipient_public_key_pem)

# Ask the user for a message to encrypt
message_to_encrypt = input("\nEnter a message to encrypt: ").encode('utf-8')

# Encrypt the message using the recipient's public key
cipher_encrypt = PKCS1_OAEP.new(recipient_public_key)
encrypted_message = cipher_encrypt.encrypt(message_to_encrypt)
encrypted_message_base64 = base64.b64encode(encrypted_message).decode('utf-8')

# Show the encrypted message in Base64
print("\nEncrypted message (Base64 Encoded):")
print(encrypted_message_base64)

# Ask the user for a message to decrypt
encrypted_message_to_decrypt_base64 = input("\nEnter a message to decrypt (Base64 Encoded): ")

# Decode the encrypted message from Base64
encrypted_message_to_decrypt = base64.b64decode(encrypted_message_to_decrypt_base64)

# Decrypt the message using the user's private key
cipher_decrypt = PKCS1_OAEP.new(key)
decrypted_message = cipher_decrypt.decrypt(encrypted_message_to_decrypt)

# Show the decrypted message
print("\nDecrypted message:")
print(decrypted_message.decode('utf-8'))

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

# Load the private key from the PEM file
with open('private_key.pem', 'rb') as f:
    private_key_pem = f.read()

# Import the private key
private_key = RSA.import_key(private_key_pem)

# Get the corresponding public key
public_key = private_key.publickey()

# Create a cipher object using the public key for encryption
cipher_rsa_enc = PKCS1_OAEP.new(public_key)

# Encrypt a message
message = b'This is a secret message.'
encrypted_message = cipher_rsa_enc.encrypt(message)
print("Encrypted message:", encrypted_message)

# Create a cipher object using the private key for decryption
cipher_rsa_dec = PKCS1_OAEP.new(private_key)

# Decrypt the message
decrypted_message = cipher_rsa_dec.decrypt(encrypted_message)
print("Decrypted message:", decrypted_message.decode('utf-8'))




from Crypto.PublicKey import RSA
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip39WordsNum
import hashlib

# Load your private key from the PEM file
with open('private_key.pem', 'rb') as f:
    private_key_pem = f.read()

# Hash the private key to get a fixed-size entropy
# Alternatively, you can use the raw key bytes directly, but hashing provides a consistent length
private_key_hash = hashlib.sha256(private_key_pem).digest()

# Generate a mnemonic phrase from the hashed private key
mnemonic = Bip39MnemonicGenerator().FromEntropy(private_key_hash)

# Print the mnemonic phrase
print("Mnemonic phrase for backup:")
print(mnemonic)

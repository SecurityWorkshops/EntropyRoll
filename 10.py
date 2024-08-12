import hashlib
import base58
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256, RIPEMD160

# Load your private key from the PEM file
with open('private_key.pem', 'rb') as f:
    private_key = RSA.import_key(f.read())

# Extract the public key from the private key
public_key = private_key.publickey().export_key(format='DER')

# Step 1: Perform SHA-256 hashing on the public key
sha256_hash = hashlib.sha256(public_key).digest()

# Step 2: Perform RIPEMD-160 hashing on the SHA-256 hash using pycryptodome
ripemd160 = RIPEMD160.new()
ripemd160.update(sha256_hash)
public_key_hash = ripemd160.digest()

# Step 3: Add version byte (0x00 for Bitcoin Mainnet)
versioned_key_hash = b'\x00' + public_key_hash

# Step 4: Perform SHA-256 hash twice on the extended RIPEMD-160 result
checksum = hashlib.sha256(hashlib.sha256(versioned_key_hash).digest()).digest()

# Step 5: Take the first 4 bytes of the second SHA-256 hash, this is the checksum
checksum = checksum[:4]

# Step 6: Add the 4 checksum bytes to the end of the extended RIPEMD-160 hash
binary_address = versioned_key_hash + checksum

# Step 7: Convert the result to a Base58 string, this is the Bitcoin address
bitcoin_address = base58.b58encode(binary_address)

# Print the Bitcoin address
print("Bitcoin Address:", bitcoin_address.decode('utf-8'))

from ecdsa import SigningKey, SECP256k1
from Crypto.Hash import SHA256, RIPEMD160
import base58

# 1. Generate an ECDSA private key using the secp256k1 curve
private_key = SigningKey.generate(curve=SECP256k1)
public_key = private_key.get_verifying_key()

# 2. Get the public key in uncompressed format (prefix with 0x04)
public_key_bytes = b'\x04' + public_key.to_string()

# 3. Hash the public key using SHA-256
sha256_hash = SHA256.new(public_key_bytes).digest()

# 4. Hash the SHA-256 result using RIPEMD-160
ripemd160_hash = RIPEMD160.new(sha256_hash).digest()

# 5. Add the version byte (0x00 for Bitcoin mainnet addresses)
version_byte = b'\x00'
extended_ripemd160 = version_byte + ripemd160_hash

# 6. Compute the checksum (SHA-256 twice and take the first 4 bytes)
checksum = SHA256.new(SHA256.new(extended_ripemd160).digest()).digest()[:4]

# 7. Append the checksum to the extended RIPEMD-160 hash
binary_address = extended_ripemd160 + checksum

# 8. Encode the result using Base58 to get the final Bitcoin address
bitcoin_address = base58.b58encode(binary_address).decode('utf-8')

# Output the results
print("Private Key (Hex):")
print(private_key.to_string().hex())

print("\nPublic Key (Uncompressed Hex):")
print(public_key_bytes.hex())

print("\nBitcoin Address:")
print(bitcoin_address)

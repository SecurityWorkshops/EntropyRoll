from Crypto.PublicKey import ECC

# Generate an ECC key pair using the secp256k1 curve
key = ECC.generate(curve='secp256k1')

# Export the private key
private_key = key.export_key(format='PEM')

# Export the public key
public_key = key.public_key().export_key(format='PEM')

print("Private Key:")
print(private_key)

print("\nPublic Key:")
print(public_key)

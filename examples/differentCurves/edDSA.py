from Crypto.PublicKey import ECC

# Generate an Ed25519 key pair
key = ECC.generate(curve='ed25519')

private_key = key.export_key(format='PEM')
public_key = key.public_key().export_key(format='PEM')

print(private_key)
print(public_key)

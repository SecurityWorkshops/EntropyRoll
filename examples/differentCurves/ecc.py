from Crypto.PublicKey import ECC

# Generate an ECC key pair
key = ECC.generate(curve='P-256')

private_key = key.export_key(format='PEM')
public_key = key.public_key().export_key(format='PEM')

print(private_key)
print(public_key)

from Crypto.PublicKey import DSA

# Generate a DSA key pair (which uses Diffie-Hellman)
key = DSA.generate(2048)

private_key = key.export_key()
public_key = key.publickey().export_key()

print(private_key.decode('utf-8'))
print(public_key.decode('utf-8'))

import hashlib
import binascii
import os
from rolls import *

from Crypto.PublicKey import RSA
from Crypto.Random import random
import random

PBKDF2_ROUNDS = 2048

# Error class 
class NotEnoughEntropy(Exception):
    pass

def dice_rolls_to_entropy(dice_rolls):
    assert all(1 <= roll <= 6 for roll in dice_rolls), "Dice rolls must be between 1 and 6"
    bits = ''.join(f'{roll-1:03b}' for roll in dice_rolls)
    if len(bits) % 8 != 0:
        bits = bits.ljust((len(bits) + 7) // 8 * 8, '0')
    entropy_bytes = int(bits, 2).to_bytes(len(bits) // 8, byteorder='big')
    return entropy_bytes

def bip39_kdf_with_custom_salt(entropy_bytes):
    password = hashlib.sha256(entropy_bytes).digest()
    derived_key = hashlib.pbkdf2_hmac(
        "sha512",
        entropy_bytes,
        password,
        PBKDF2_ROUNDS,
        32  # 32 bytes = 256 bits of entropy
    )
    return derived_key

def generate_rsa_keypair(dice_rolls):
    size = len(dice_rolls)
    if size < 100:
        raise NotEnoughEntropy("Not enough entropy!")
    
    entropy = dice_rolls_to_entropy(dice_rolls)
    derived_key = bip39_kdf_with_custom_salt(entropy)

    print(f"Size of derived_key: {len(derived_key)} bytes")
    print(f"Number of dice rolls: {size}")
    print("Entropy:", binascii.hexlify(entropy))
    print("Derived Key:", binascii.hexlify(derived_key))
    
    # Use derived_key to seed a secure RNG
    rng = random.Random(derived_key)

    def custom_rng(n):
        return rng.getrandbits(n * 8).to_bytes(n, 'big')

    # Generate the RSA key using the custom RNG
    RSAkey = RSA.generate(2048, randfunc=custom_rng)

    private_key = RSAkey.export_key()
    public_key = RSAkey.publickey().export_key()

    print(private_key.decode('utf-8'))
    print(public_key.decode('utf-8'))

    # Save the private key to a file
    with open('private_key.pem', 'wb') as f:
        f.write(private_key)

# Example usage:
generate_rsa_keypair(dice_rolls)

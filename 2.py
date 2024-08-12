import hashlib
import binascii
from rolls import *



PBKDF2_ROUNDS = 2048

def dice_rolls_to_entropy(dice_rolls):
    # Ensure dice rolls are integers between 1 and 6
    assert all(1 <= roll <= 6 for roll in dice_rolls), "Dice rolls must be between 1 and 6"
    
    # Convert dice rolls to bits
    bits = ''.join(f'{roll-1:03b}' for roll in dice_rolls)  # 3 bits per roll
    
    # Pad bits to make sure length is divisible by 8 (byte-aligned)
    if len(bits) % 8 != 0:
        bits = bits.ljust((len(bits) + 7) // 8 * 8, '0')
    
    # Convert bits to entropy (as bytes)
    entropy_bytes = int(bits, 2).to_bytes(len(bits) // 8, byteorder='big')
    
    return entropy_bytes

def bip39_kdf_with_custom_salt(entropy_bytes):
    # Generate a SHA-256 hash of the dice rolls to use as a password/salt
    password = hashlib.sha256(entropy_bytes).digest()
    
    # Derive the entropy using PBKDF2 with HMAC-SHA512
    derived_key = hashlib.pbkdf2_hmac(
        "sha512",
        entropy_bytes,
        password,
        PBKDF2_ROUNDS,
        32,  # 32 bytes = 256 bits of entropy
    )
    
    return derived_key

# Example usage

entropy = dice_rolls_to_entropy(dice_rolls)
derived_key = bip39_kdf_with_custom_salt(entropy)

print("Entropy:", binascii.hexlify(entropy))
print("Derived Key:", binascii.hexlify(derived_key))

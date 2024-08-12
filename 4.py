import hashlib
import binascii
from rolls import *

PBKDF2_ROUNDS = 2048
from Crypto.PublicKey import RSA

# Error class 
class NotEnoughEntropy(Exception):
    pass

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
        256  # 256 bytes = 2048 bits of entropy needed for RSA 2048-bit key
    )
    
    return derived_key

def generate_rsa_keypair(dice_rolls):
    size = len(dice_rolls)
    
    if size < 100:
        raise NotEnoughEntropy("Not enough entropy!")

    entropy = dice_rolls_to_entropy(dice_rolls)
    derived_key = bip39_kdf_with_custom_salt(entropy)

    # Check the size of the derived key
    derived_key_size = len(derived_key)
    print(f"Size of derived_key: {derived_key_size} bytes")

    if derived_key_size < 256:
        raise NotEnoughEntropy(f"Derived key is too small: {derived_key_size} bytes (Need at least 256 bytes)")

    print(f"Number of dice rolls: {size}")
    print("Entropy:", binascii.hexlify(entropy))
    print("Derived Key:", binascii.hexlify(derived_key))

    # Redefine the custom_rng function to use derived_key properly
    index = 0

    def custom_rng(n):
        nonlocal index
        if index + n > len(derived_key):
            raise ValueError("Not enough entropy provided!")
        result = derived_key[index:index+n]
        index += n
        return result

    # Generate the RSA key using the custom RNG
    RSAkey = RSA.generate(2048, randfunc=custom_rng)

    # Export the private and public keys
    private_key = RSAkey.export_key()
    public_key = RSAkey.publickey().export_key()

    print(private_key.decode('utf-8'))
    print(public_key.decode('utf-8'))


# Example usage:
# dice_rolls = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6] * 10  # Example dice rolls
generate_rsa_keypair(dice_rolls)

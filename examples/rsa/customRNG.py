from Crypto.PublicKey import RSA
from Crypto.Util import number

#for demo 
import random 

# Example: Dice rolls - Convert these to a byte string
# Let's assume each roll is between 1 and 6.
dice_rolls = [4, 6, 3, 2, 5, 1, 6, 3, 4, 2]  # Example rolls

#Simulate rolling 100 dice, each with a value between 1 and 6
dice_rolls = [random.randint(1, 6) for _ in range(100)]

# Convert dice rolls to a binary string, assuming each roll is mapped to 3 bits
# (as 3 bits can represent numbers from 1 to 6).
bit_string = ''.join([format(roll - 1, '03b') for roll in dice_rolls])

# Calculate the required length to make the bit string a multiple of 8
required_length = (len(bit_string) + 7) // 8 * 8

# Pad the bit string with leading zeros if necessary
padded_bit_string = bit_string.zfill(required_length)

# Convert the padded bit string to a byte array
entropy_bytes = int(padded_bit_string, 2).to_bytes(len(padded_bit_string) // 8, byteorder='big')


# Function to simulate random number generator using the dice rolls
def custom_rng(n):
    # Return `n` bytes from the entropy pool
    if len(entropy_bytes) < n:
        print(f"n needed: {n} current {len(entropy_bytes)}")
        raise ValueError("Not enough entropy!")
    return entropy_bytes[:n]

# Generate the RSA key using the custom RNG
RSAkey = RSA.generate(2048, randfunc=custom_rng)

# Now you can export or use the key as needed
private_key = RSAkey.export_key()
public_key = RSAkey.publickey().export_key()

print(private_key.decode('utf-8'))

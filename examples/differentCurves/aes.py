from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(32)  # 256-bit key
cipher = AES.new(key, AES.MODE_GCM)

nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(b'Your message here')

print(f'Ciphertext: {ciphertext}')

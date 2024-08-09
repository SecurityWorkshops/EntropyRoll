## Bitcoin Addresses

Bitcoin addresses are generated as follows:

Generate the public key.
Hash the public key using SHA-256.
Hash the result using RIPEMD-160.
Add a version byte (for Bitcoin, it's typically 0x00 for a mainnet address).
Compute the checksum by hashing twice with SHA-256 and taking the first 4 bytes.
Append the checksum to the hashed public key.
Encode the result using Base58 to get the Bitcoin address.


Bitcoin was the first cryptocurrency. 
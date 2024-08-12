from bip_utils import Bip39MnemonicValidator, Bip39MnemonicDecoder

# Example mnemonic (use the one you generated)
mnemonic_phrase = "your generated mnemonic phrase here"

# Validate the mnemonic phrase
if Bip39MnemonicValidator().IsValid(mnemonic_phrase):
    # Decode the mnemonic back into entropy (hash)
    decoded_entropy = Bip39MnemonicDecoder().Decode(mnemonic_phrase)

    # Now you'd typically map this back to your private key
    # Since we used a hash, you'd need to store the original PEM file securely, but this shows how it works
    restored_key_hash = decoded_entropy[:32]  # SHA-256 produces 32 bytes

    # Print the restored key hash (for demonstration)
    print("Restored key hash:")
    print(restored_key_hash.hex())
else:
    print("Invalid mnemonic phrase!")

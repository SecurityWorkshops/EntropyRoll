from Crypto.PublicKey import RSA
from Crypto import Random
import pathlib
import base64
from Crypto.Cipher import PKCS1_OAEP
import pickle
import uuid

class SimpleEncryption:
    def __init__(self):
        self.version = "0.1"
        self.key = None
        self.mySettings = self.load_config()

    def load_config(self):
        config_path = pathlib.Path("settings.ini")
        if config_path.exists():
            with config_path.open("rb") as file:
                my_settings = pickle.load(file)
        else:
            my_settings = {
                "UUID": uuid.uuid4().hex,
                "vault": []
            }
        return my_settings

    def save_config(self):
        with pathlib.Path("settings.ini").open("wb") as file:
            pickle.dump(self.mySettings, file)

    def generate_key(self):
        rsa_key = RSA.generate(2048, Random.new().read)
        priv_key_path = pathlib.Path("keys/my.pem")
        priv_key_path.parent.mkdir(parents=True, exist_ok=True)
        with priv_key_path.open("wb") as file:
            file.write(rsa_key.export_key('PEM'))

    def load_private_key(self, location="keys/my.pem"):
        with pathlib.Path(location).open("r") as file:
            self.key = RSA.import_key(file.read())

    def export_public_key(self):
        return self.key.publickey().export_key()

    def encrypt_message(self, message, public_key):
        encryptor = PKCS1_OAEP.new(RSA.import_key(public_key))
        encrypted = encryptor.encrypt(message.encode())
        return base64.b64encode(encrypted)

    def decrypt_message(self, message):
        cipher = PKCS1_OAEP.new(self.key)
        decrypted = cipher.decrypt(base64.b64decode(message))
        return decrypted

    def add_to_vault(self, public_key, nickname):
        vault_entry = {
            "id": str(uuid.uuid4()),
            "nickname": nickname,
            "pub": public_key
        }
        self.mySettings["vault"].append(vault_entry)
        return vault_entry

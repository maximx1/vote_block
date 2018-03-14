from Crypto.PublicKey import ECC

def generate_key_pair(passphrase):
    key = ECC.generate(curve='P-256')
    private_key = key.export_key(passphrase=passphrase, format='PEM', protection="PBKDF2WithHMAC-SHA1AndAES128-CBC")
    public_key = key.public_key().export_key(format='OpenSSH')
    return (public_key, private_key)

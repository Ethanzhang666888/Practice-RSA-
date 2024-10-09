from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def rsa_signature(nickname, nonce):

    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    

    message = f"{nickname}{nonce}".encode()
    hash_message = SHA256.new(message)
    signature = pkcs1_15.new(key).sign(hash_message)

    print(f"签名: {signature.hex()}")


    try:
        pkcs1_15.new(key.publickey()).verify(hash_message, signature)
        print("签名验证成功。")
    except (ValueError, TypeError):
        print("签名验证失败。")
    
    return private_key, public_key

nickname = "Ethanzhang666888"
nonce = 12345 
private_key, public_key = rsa_signature(nickname, nonce)

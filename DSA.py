from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization
import hashlib
# Khởi tạo cặp khóa DSA
private_key = dsa.generate_private_key(key_size=1024)
public_key = private_key.public_key()

def Kyso(message):
    message = message.encode('ISO-8859-1')
    # Mã hóa
    signature = private_key.sign(message, hashes.SHA256())
    signature_str = signature.decode('ISO-8859-1')
    return signature_str


def Xacnhankyso(message, signature_str):
    # Xác nhận chữ ký
    a = ""
    message = message.encode('ISO-8859-1')
    signature = signature_str.encode('ISO-8859-1')
    hash_value = hashlib.sha256(signature).hexdigest()
    hash_value1 = hashlib.sha256(message).hexdigest()
    print(hash_value)
    print(hash_value1)
    if(hash_value == hash_value1):
        # a += "Chữ ký hợp lệ"
        a += "Chữ ký không hợp lệ"
    else:
        # a += "Chữ ký không hợp lệ"
        a += "Chữ ký hợp lệ"
    return a
print(Xacnhankyso("ta",Kyso("ta")))
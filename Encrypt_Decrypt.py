import os
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

def get_key(password):
    password = password.encode()
    salt = b'giangllt_'  # Bạn có thể thay đổi salt này
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open(file_path + '.encrypted', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    os.remove(file_path)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(data)
        with open(file_path[:-10], 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
        os.remove(file_path)
        return True
    except InvalidToken:
        print(f"Sai mật khẩu hoặc file bị hỏng: {file_path}")
        return False

def process_folder(folder_path, password, mode):
    key = get_key(password)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if mode == 'encrypt' and not file.endswith('.encrypted'):
                encrypt_file(file_path, key)
                print(f"Đã mã hóa: {file_path}")
            elif mode == 'decrypt' and file.endswith('.encrypted'):
                if decrypt_file(file_path, key):
                    print(f"Đã giải mã: {file_path}")

# Sử dụng
folder_path = input("Nhập đường dẫn thư mục: ")
password = input("Nhập mật khẩu: ")
mode = input("Chọn chế độ (encrypt/decrypt): ").lower()

if mode in ['e', 'd']:
    if mode == "e":
        mode = "encrypt"
    elif  mode == "d":
        mode = "decrypt"
        
    process_folder(folder_path, password, mode)
else:
    print("Chế độ không hợp lệ. Vui lòng chọn 'encrypt' hoặc 'decrypt'.")
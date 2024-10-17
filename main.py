from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Encrypt a message
def encrypt_message(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    return iv + ciphertext

# Decrypt a message
def decrypt_message(key, ciphertext):
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode('utf-8')

# Encrypt a file
def encrypt_file(key, input_file, output_file):
    with open(input_file, 'rb') as file:
        data = file.read()
    encrypted_data = encrypt_message(key, data.decode('utf-8'))
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

# Decrypt a file
def decrypt_file(key, input_file, output_file):
    with open(input_file, 'rb') as file:
        data = file.read()
    decrypted_data = decrypt_message(key, data)
    with open(output_file, 'w') as file:
        file.write(decrypted_data)

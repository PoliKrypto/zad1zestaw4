from utils.desx_encryption import DesxEncryption

encryptor = DesxEncryption('dupadupa', 'dupadupa', 'dupadupa')

with open ("logo.png", "r") as myfile:
    data = myfile.readlines()

text = encryptor.desx(data, decoding=False)
print(data)
print(text)
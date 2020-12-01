from utils.desx_encryption import DesxEncryption

encryptor = DesxEncryption('dupadupa', 'dupadupa', 'dupadupa')

with open ("mati.pdf", "rb") as myfile:
    data = myfile.read()

print('MAAAAIIIIINNNNN')
print("------------------------------")
print(data[:50])

text = encryptor.desx(data.decode('latin1'), decoding=False)
print(text[:100])


decoded = encryptor.desx(text, decoding=True)

print(decoded[:50])
print(type(decoded))

f = open("twojastara.pdf", "wb")
f.write(decoded)
f.close()
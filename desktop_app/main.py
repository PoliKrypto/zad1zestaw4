import json
import string
import tkinter as tk
import random
from tkinter.filedialog import askopenfilename

from utils.desx_encryption import DesxEncryption


class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()

	def create_widgets(self):

		self.key1_label = tk.Label(self, text='KEY 1')
		self.key1_label.pack(side='top')
		self.key1 = tk.Text(self, height=1, width=10, font=('Arial', 14), bg='grey')
		self.key1.pack(side='top')

		self.key2_label = tk.Label(self, text='KEY 2')
		self.key2_label.pack(side='top')
		self.key2 = tk.Text(self, height=1, width=10, font=('Arial', 14), bg='grey')
		self.key2.pack(side='top')

		self.key3_label = tk.Label(self, text='KEY 3')
		self.key3_label.pack(side='top')
		self.key3 = tk.Text(self, height=1, width=10, font=('Arial', 14), bg='grey')
		self.key3.pack(side='top')

		self.keygen = tk.Button(self, text='GENERATE KEYS', command=self.keygen)
		self.keygen.pack(side='top')

		self.save_keys = tk.Button(self, text='SAVE KEYS', command=self.save_keys)
		self.save_keys.pack(side='top')

		self.read_keys = tk.Button(self, text='READ KEYS', command=self.read_keys)
		self.read_keys.pack(side='top')

		self.input_label = tk.Label(self, text='INPUT')
		self.input_label.pack(side='left')
		self.input = tk.Text(self, height=10, width=20, font=('Arial', 30), bg='grey')
		self.input.pack(side='left')

		self.output_label = tk.Label(self, text='OUTPUT')
		self.output_label.pack(side='right')
		self.output = tk.Text(self, height=10, width=20, font=('Arial', 30), bg='grey')
		self.output.pack(side='right')

		self.encypt = tk.Button(self, text='ENCODE FILE', command=self.encrypt_file)
		self.encypt.pack(side='bottom')

		self.encypt = tk.Button(self, text='DECODE FILE', command=self.decrypt_file)
		self.encypt.pack(side='bottom')

		self.encypt = tk.Button(self, text='>>>', command=self.encrypt)
		self.encypt.pack(side='bottom')

		self.decrypt = tk.Button(self, text='<<<', command=self.decrypt)
		self.decrypt.pack(side='bottom')

	def get_random_alphanumeric_string(self, length):
		letters_and_digits = string.ascii_letters + string.digits
		result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
		return result_str

	def keygen(self):
		self.key1.insert(index='1.0', chars=self.get_random_alphanumeric_string(8))
		self.key2.insert(index='1.0', chars=self.get_random_alphanumeric_string(8))
		self.key3.insert(index='1.0', chars=self.get_random_alphanumeric_string(8))

	def save_keys(self):
		data = {
			'key1': self.key1.get('1.0', tk.END)[:-1],
			'key2': self.key2.get('1.0', tk.END)[:-1],
			'key3': self.key3.get('1.0', tk.END)[:-1]
		}

		with open('keys.json', 'w') as file:
			json.dump(data, file)

	def read_keys(self):
		filename = askopenfilename()
		with open(filename) as json_file:
			data = json.load(json_file)
			self.key1.insert(index='1.0', chars=data['key1'])
			self.key2.insert(index='1.0', chars=data['key2'])
			self.key3.insert(index='1.0', chars=data['key3'])

	def encrypt(self):
		text = self.input.get('1.0', tk.END)[:-1]
		key1 = self.key1.get('1.0', tk.END)[:-1]
		key2 = self.key2.get('1.0', tk.END)[:-1]
		key3 = self.key3.get('1.0', tk.END)[:-1]

		encryptor = DesxEncryption(key1, key2, key3)

		binary_cipher = encryptor.desx(text)

		self.output.delete('1.0', tk.END)
		self.output.insert(index='1.0', chars=binary_cipher)

	def encrypt_file(self):
		filename = askopenfilename()
		key1 = self.key1.get('1.0', tk.END)[:-1]
		key2 = self.key2.get('1.0', tk.END)[:-1]
		key3 = self.key3.get('1.0', tk.END)[:-1]

		with open(filename, "rb") as file:
			data = file.read()

		encryptor = DesxEncryption(key1, key2, key3)
		text = encryptor.desx(data.decode('latin1'), decoding=False)

		f = open(filename + '.desx', "w")
		f.write(text)
		f.close()

	def decrypt(self):
		text = self.output.get('1.0', tk.END)
		key1 = self.key1.get('1.0', tk.END)[:-1]
		key2 = self.key2.get('1.0', tk.END)[:-1]
		key3 = self.key3.get('1.0', tk.END)[:-1]

		# delete the newline from text field
		text = text[:-1]
		encryptor = DesxEncryption(key1, key2, key3)
		message = encryptor.desx(text, decoding=True)

		self.input.delete('1.0', tk.END)
		self.input.insert(index='1.0', chars=message.decode('latin1'))

	def decrypt_file(self):
		filename = askopenfilename()
		key1 = self.key1.get('1.0', tk.END)[:-1]
		key2 = self.key2.get('1.0', tk.END)[:-1]
		key3 = self.key3.get('1.0', tk.END)[:-1]

		with open(filename, "r") as file:
			data = file.read()

		encryptor = DesxEncryption(key1, key2, key3)
		decoded = encryptor.desx(data, decoding=True)

		f = open(filename[:len(filename)-5], "wb")
		f.write(decoded)
		f.close()


root = tk.Tk()
app = Application(master=root)

app.mainloop()

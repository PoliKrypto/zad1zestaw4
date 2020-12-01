
from . import desx_helpers as helpers
from . import desx_keygen_helpers as keygen_helpers


class DesxEncryption:

	def __init__(self, key1txt, key2txt, key3txt):
		self.key1 = keygen_helpers.key_64bit(key1txt)
		self.key2 = keygen_helpers.key_64bit(key2txt)
		self.key3 = keygen_helpers.key_64bit(key3txt)

	def desx(self, text, decoding=False):

		# print('debug')
		# print()
		# print(type())

		if decoding:
			output = ''
			text = text.encode().decode('latin1')
			cipher_blocks = helpers.split_message(text, 64)
			for block in cipher_blocks:
				cipher_block_xored = helpers.xor(block, self.key3)
				permutated_cipher_block = keygen_helpers.key_permutation(cipher_block_xored, helpers.IP)
				message = self.des(permutated_cipher_block, decoding=True)
				message = helpers.xor(message, self.key1)
				message = helpers.split_message(message, 8)
				for byte in message:
					output += (chr(int(byte, 2)))
			return output.encode('latin1')
			#return output

		else:
			# print('debug 1')
			# print(text)
			# print(type(text))
			# xd = text.encode()
			# print(xd)
			# print(xd.decode('latin1'))

			# text = text.encode().decode('latin1')

			message_blocks = helpers.split_message(text, 8)

			# print('debug 2')
			# print(message_blocks)
			# print(type(message_blocks))

			binary_blocks = helpers.binary_message_blocks(message_blocks)

			# print('debug 3')
			# print(binary_blocks)
			# print(type(binary_blocks))

			binary_cipher_blocks = []
			for index, block in enumerate(binary_blocks):
				binary_block_xored = helpers.xor(binary_blocks[index], self.key1)
				permutated_binary_block = keygen_helpers.key_permutation(binary_block_xored, helpers.IP)
				binary_cipher = self.des(permutated_binary_block)
				binary_block_xored = helpers.xor(binary_cipher, self.key3)
				binary_cipher_blocks.append(binary_block_xored)
			binary_cipher = ''.join(binary_cipher_blocks)
			return binary_cipher

	def des(self, word, decoding=False):
		cipher = ''
		left = word[:32]
		right = word[32:]
		sub_keys = []

		if decoding:
			for i in reversed(keygen_helpers.keys_generator(self.key2)):
				sub_keys.append(i)
		else:
			sub_keys = keygen_helpers.keys_generator(self.key2)

		for sub_key in sub_keys:
			perm_right = keygen_helpers.key_permutation(right, helpers.E_BIT)
			xor_right = helpers.xor(perm_right, sub_key)
			xor_blocks = helpers.split_message(xor_right, 6)
			perm_s_right = keygen_helpers.perm_s(xor_blocks)
			perm2_right = keygen_helpers.key_permutation(perm_s_right, helpers.P)
			buf = right
			right = helpers.xor(perm2_right, left)
			left = buf

		buf = right
		right = left
		left = buf
		new = left + right
		cipher += keygen_helpers.key_permutation(new, helpers.IP2)
		return cipher

from . import desx_helpers as helpers
from . import desx_keygen_helpers as keygen_helpers


class DesxEncryption:

	def __init__(self, key1txt, key2txt, key3txt):
		self.key1 = keygen_helpers.key_64bit(key1txt)
		self.key2 = keygen_helpers.key_64bit(key2txt)
		self.key3 = keygen_helpers.key_64bit(key3txt)

	def desx(self, text, decoding=False):

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

		else:
			# dzielimy 64 bajtowy blok danych na bloki 8 bajtowe
			message_blocks = helpers.split_message(text, 8)
			# zamieniamy bloki danych na bloki binarne
			binary_blocks = helpers.binary_message_blocks(message_blocks)
			binary_cipher_blocks = []
			# iterujemy bo bitowych blokach danych
			for index, block in enumerate(binary_blocks):
				# operacja XOR z kluczem 1
				binary_block_xored = helpers.xor(binary_blocks[index], self.key1)
				# permutacja początkowa do DES
				permutated_binary_block = keygen_helpers.key_permutation(binary_block_xored, helpers.IP)
				# DES (używany jest klucz 2)
				binary_cipher = self.des(permutated_binary_block)
				# operacja XOR z kluczem 3
				binary_block_xored = helpers.xor(binary_cipher, self.key3)
				binary_cipher_blocks.append(binary_block_xored)
			binary_cipher = ''.join(binary_cipher_blocks)
			return binary_cipher

	# word - 8 bajtowy blok danych
	def des(self, word, decoding=False):
		cipher = ''
		# dzielimy blok na 2 części
		left = word[:32]
		right = word[32:]
		sub_keys = []
		# generujemy 16 podkluczy
		if decoding:
			# odwrotna kolejność przy rozszyfrowywaniu
			for i in reversed(keygen_helpers.keys_generator(self.key2)):
				sub_keys.append(i)
		else:
			# normalna kolejność przy szyfrowaniu
			sub_keys = keygen_helpers.keys_generator(self.key2)
		# iterujemy po wszystkich podkluczach
		for sub_key in sub_keys:
			# rozszerzamy prawą stronę z 32 do 48 bitów
			perm_right = keygen_helpers.key_permutation(right, helpers.E_BIT)
			# operacja XOR bloku danych (48 bitów) z podkluczem (również 48 bitów)
			xor_right = helpers.xor(perm_right, sub_key)
			# dzielimy 48 bitowy blok na osiem 6 bitowych bloków
			xor_blocks = helpers.split_message(xor_right, 6)
			# każdy blok podawany jest na wejście jednego z S-bloków
			# (pierwszy 6-bitowy blok na wejście pierwszego S-bloku, drugi 6-bitowy blok na wejście drugiego S-bloku itd.)
			perm_s_right = keygen_helpers.perm_s(xor_blocks)
			# wyjście S-bloków poddawane jest permutacji w P-blokach
			perm2_right = keygen_helpers.key_permutation(perm_s_right, helpers.P)
			# chwilowe przechowanie prawej strony bloku
			buf = right
			# operacja XOR z lewą połową bloku
			right = helpers.xor(perm2_right, left)
			# lewa strona bloku przyjmuje wartości prawej strony
			left = buf

		buf = right
		right = left
		left = buf
		new = left + right
		cipher += keygen_helpers.key_permutation(new, helpers.IP2)
		return cipher
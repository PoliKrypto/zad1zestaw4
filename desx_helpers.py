import desx_keygen_helpers as keygen_helpers


IP = (58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7)

P = (16, 7, 20, 21,
     29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2, 8, 24, 14,
     32, 27, 3, 9,
     19, 13, 30, 6,
     22, 11, 4, 25)

IP2 = (40, 8, 48, 16, 56, 24, 64, 32,
       39, 7, 47, 15, 55, 23, 63, 31,
       38, 6, 46, 14, 54, 22, 62, 30,
       37, 5, 45, 13, 53, 21, 61, 29,
       36, 4, 44, 12, 52, 20, 60, 28,
       35, 3, 43, 11, 51, 19, 59, 27,
       34, 2, 42, 10, 50, 18, 58, 26,
       33, 1, 41, 9, 49, 17, 57, 25)

E_BIT = (32, 1, 2, 3, 4, 5,
         4, 5, 6, 7, 8, 9,
         8, 9, 10, 11, 12, 13,
         12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21,
         20, 21, 22, 23, 24, 25,
         24, 25, 26, 27, 28, 29,
         28, 29, 30, 31, 32, 1)


def split_message(message, n):
    if len(message) % n != 0:
        message += '\0' * (n - len(message) % n)
    blocks_amount = len(message) // n
    message_blocks = [''] * blocks_amount
    i = 0
    n_block = 0
    for letter in message:
        i += 1
        message_blocks[n_block] += letter
        if i % n == 0:
            i = 0
            n_block += 1
    return message_blocks


def binary_message_blocks(message_blocks):
    blocks_amount = len(message_blocks)
    bin_blocks = [''] * blocks_amount
    for i, block in enumerate(bin_blocks):
        bin_blocks[i] += keygen_helpers.key_64bit(message_blocks[i])
    return bin_blocks


def xor(series1, series2):
    result = ''
    for i, bit in enumerate(series1):
        if bit == '0' and series2[i] == '0':
            result += '0'
        elif bit == '1' and series2[i] == '1':
            result += '0'
        else:
            result += '1'
    return result

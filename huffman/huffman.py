from collections import Counter
from collections import namedtuple
import heapq


class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def get_frequency():
    frequency = {}

    def add_letter(letter=None):
        if letter is None:
            return frequency
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    return add_letter


def get_map(letter_map={}):
    queue = []
    for letter, frequency in letter_map.items():
        queue.append((frequency, len(queue), Leaf(letter)))
    heapq.heapify(queue)
    count = len(queue)

    while len(queue) > 1:
        freq1, _, left = heapq.heappop(queue)
        freq2, _, right = heapq.heappop(queue)
        heapq.heappush(queue, (freq1 + freq2, count, Node(left, right)))

        count += 1
    codes_map = {}
    if queue:
        [(_freq, _, root)] = queue
        root.walk(codes_map, '')
    return codes_map


def encode(codes_map):
    last_bits = ''
    file = open('huffman/encoded', 'wb')
    max_elem = max(codes_map.values(), key=lambda letter: len(letter))
    for i in range(8, 32, 8):
        if i - 8 < len(max_elem) < i:
            max_len = i

    def add_letter(letter=None):
        nonlocal last_bits
        if letter is None:
            need_zeros = 8 - len(last_bits)
            last_bits = last_bits.ljust(8, '0')
            byte = bytes([int(last_bits, 2)])
            file.write(byte)
            byte = bytes([need_zeros])
            file.write(byte)
            file.close()
            file_codes = open('huffman/codes', 'wb')
            file_codes.write(bytes([max_len // 8]))
            print(bytes([max_len // 8]), max_len // 8)
            for letter, code in codes_map.items():
                need_zeros = max_len - len(code)
                code = code.ljust(max_len, '0')
                file_codes.write(bytes([need_zeros]))
                while code:
                    file_codes.write(bytes([int(code[:8], 2)]))
                    code = code[8:]
                file_codes.write(letter.encode())
            return
        last_bits += codes_map[letter]
        if len(last_bits) > 8:
            byte = bytes([int(last_bits[:8], 2)])
            last_bits = last_bits[8:]
            file.write(byte)
    return add_letter


def huffman_decode(codes_map={}):
    file_codes = open('huffman/codes', 'rb')
    code_size = None
    with open('huffman/codes', 'rb') as f:
        byte = f.read(1)
        while byte != '':
            if code_size is not None:
                break
            else:
                code_size = int.from_bytes(byte, byteorder='little')
            byte = f.read(1)

    encoded = []

    letters_map = {}
    for letter, code in codes_map.items():
        letters_map[code] = letter

    file_in = open('huffman/encoded', 'rb')
    encoded_ch = ''

    last_pos = list(file_in)[::-1]
    last_zeros = last_pos[0][len(last_pos[0]) - 1]
    file_in.seek(0, 0)
    for line in file_in:
        for byte in line:
            encoded_ch += str(bin(byte))[2:].rjust(8, '0')
    file_in.close()
    encoded_ch = encoded_ch[:len(encoded_ch) - 8 - last_zeros]
    while encoded_ch:
        for i in range(1, len(encoded_ch) + 1):
            if encoded_ch[:i] in letters_map:
                encoded.append(letters_map[encoded_ch[:i]])
                encoded_ch = encoded_ch[i:]
                break

    file_out = open('huffman/decoded', 'w')
    file_out.write(''.join(encoded))
    file_out.close()

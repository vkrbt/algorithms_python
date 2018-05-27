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

    def add_letter(letter=None):
        nonlocal last_bits
        if letter is None:
            need_zeros = 8 - len(last_bits)
            last_bits = last_bits.ljust(8, '0')
            byte = bytes([int(last_bits, 2)])
            file.write(byte)
            byte = bytes([need_zeros])
            print(need_zeros)
            file.write(byte)
            file.close()
            return
        last_bits += codes_map[letter]
        if len(last_bits) > 8:
            byte = bytes([int(last_bits[:8], 2)])
            last_bits = last_bits[8:]
            file.write(byte)
    return add_letter


def huffman_decode(codes_map):
    encoded = []
    file_in = open('huffman/encoded', 'rb')
    encoded_ch = ''

    last_pos = list(file_in)[::-1]
    last_zeros = last_pos[0][len(last_pos[0]) - 1]
    file_in.seek(0, 0)
    for line in file_in:
        for byte in line:
            encoded_ch += str(bin(byte))[2:].rjust(8, '0')
    encoded_ch = encoded_ch[:len(encoded_ch) - 8 - last_zeros]
    while encoded_ch:
        for i in range(1, len(encoded_ch) + 1):
            for letter, code in codes_map.items():
                if code == encoded_ch[:i]:
                    encoded.append(letter)
                    encoded_ch = encoded_ch[i:]

    file_out = open('huffman/decoded', 'w')
    file_out.write(''.join(encoded))

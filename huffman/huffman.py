from collections import Counter  # словарь в котором для каждого объекта поддерживается счетчик
from collections import namedtuple
import heapq


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"

def get_frequency():
    frequency = {}
    def add_letter(letter = None):
        if letter is None:
            return frequency
        if letter in frequency:
            frequency[letter] += 1
        else:
            frequency[letter] = 1
    return add_letter

def get_map(letter_map = {}):
    h = []
    for letter, frequency in letter_map.items():
        h.append((frequency, len(h), Leaf(letter)))
    heapq.heapify(h)
    count = len(h)

    while len(h) > 1:
        freq1, _, left = heapq.heappop(h)
        freq2, _, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))

        count += 1
    codes_map = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(codes_map, "")
    return codes_map

def encode(codes_map):
    encoded = ''
    def add_letter(letter = None):
        if letter is None:
            return encoded    
        encoded += codes_map[letter]
    return add_letter

def huffman_decode(encoded, code):  # функция декодирования исходной строки по кодам Хаффмана
    sx =[]  # инициализируем массив символов раскодированной строки
    enc_ch = ""  # инициализируем значение закодированного символа
    for ch in encoded:  # обойдем закодированную строку по символам
        enc_ch += ch  # добавим текущий символ к строке закодированного символа
        for dec_ch in code:  # постараемся найти закодированный символ в словаре кодов
            if code.get(dec_ch) == enc_ch:  # если закодированный символ найден,
                sx.append(dec_ch)  # добавим значение раскодированного символа к массиву раскодированной строки
                enc_ch = ""  # обнулим значение закодированного символа
                break
    return "".join(sx)
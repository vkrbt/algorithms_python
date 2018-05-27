from huffman import get_frequency, get_map, encode

if __name__ == '__main__':
    file  = open('huffman/text.txt', 'r')
    add_letter = get_frequency()
    for line in file:
        for ch in line:
            add_letter(ch)
    file.close()
    
    codes_map = add_letter()

    encoded = encode(codes_map)
                                             # в соответствующий код и конкатенируем результат
    print(len(codes_map), len(encoded))  # выведем число символов и длину закодированной строки
    for ch in sorted(codes_map): # обойдем символы в словаре в алфавитном порядке с помощью функции sorted()
        print("{}: {}".format(ch, codes_map[ch]))  # выведем символ и соответствующий ему код
    print(encoded)
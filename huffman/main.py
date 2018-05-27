from huffman import get_frequency, get_map, encode, huffman_decode

if __name__ == '__main__':
    file = open('huffman/text.txt', 'r')
    add_letter = get_frequency()
    for line in file:
        for ch in line:
            add_letter(ch)
    file.close()

    codes_map = get_map(add_letter())

    add_letter = encode(codes_map)
    file = open('huffman/text.txt', 'r')
    for line in file:
        for ch in line:
            add_letter(ch)
    add_letter()
    file.close()
    huffman_decode(codes_map)

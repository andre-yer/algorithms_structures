from collections import Counter


def modify_dict(symbols_dict, temp_dict, symbol, modifier):
    ans = 0
    if symbol not in temp_dict:
        temp_dict[symbol] = 0
    if symbol in symbols_dict and symbols_dict[symbol] == temp_dict[symbol]:
        ans = -1
    temp_dict[symbol] += modifier
    if symbol in symbols_dict and symbols_dict[symbol] == temp_dict[symbol]:
        ans = 1
    return ans


def maya(len_word, len_seq, word, sequence):
    symbols_dict = Counter(word)
    temp_dict = Counter(sequence[:len_word])
    match = 0
    result = 0

    for key, value in symbols_dict.items():
        if value == temp_dict[key]:
            match += 1
    if match == len(symbols_dict):
        result += 1

    for i in range(len_word, len_seq):
        match += modify_dict(symbols_dict, temp_dict,
                             sequence[i - len_word], -1)
        match += modify_dict(symbols_dict, temp_dict, sequence[i], 1)
        if match == len(symbols_dict):
            result += 1

    return result


def main():
    with open('input.txt', 'r') as file:
        len_word, len_seq = map(int, file.readline().strip().split())
        word = file.readline().strip()
        sequence = file.readline().strip()
    print(maya(len_word, len_seq, word, sequence))


if __name__ == '__main__':
    main()

import sys


def freq_use_word(words_list):
    words_dict = {}
    max_value = 0
    for item in words_list:
        if item not in words_dict:
            words_dict[item] = 0
        words_dict[item] += 1
        if words_dict[item] > max_value:
            max_value = words_dict[item]
    return sorted([k for k, v in words_dict.items() if v == max_value])[0]


def main():
    words_list = sys.stdin.read().split()
    print(freq_use_word(words_list))


if __name__ == '__main__':
    main()

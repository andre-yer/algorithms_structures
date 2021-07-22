import sys


def make_words_list(line_list):
    words_list = []
    for line in line_list:
        for item in line:
            words_list.append(item)
    return words_list


def unique_words(words_list):
    return len(set(words_list))


def main():
    line_list = []
    for line in sys.stdin:
        if not line or line == '\n':
            break
        else:
            line_list.append(line.split())
    print(unique_words(make_words_list(line_list)))


if __name__ == '__main__':
    main()

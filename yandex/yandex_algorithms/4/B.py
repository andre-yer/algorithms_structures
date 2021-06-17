import sys


def count_words(words_list):
    words_dict = {}
    answer_list = []
    for item in words_list:
        if item not in words_dict:
            words_dict[item] = 0
        answer_list.append(str(words_dict[item]))
        words_dict[item] += 1
    return ' '.join(answer_list)


words_list = sys.stdin.read().split()
print(count_words(words_list))

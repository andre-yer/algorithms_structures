def get_list():
    numbers = []
    while True:
        item = int(input())
        if item == -2_000_000_000:
            break
        else:
            numbers.append(item)
    return numbers


def check_list(numbers):
    const = True
    asc = True
    weak_asc = True
    desc = True
    weak_desc = True
    for i in range(1, len(numbers)):
        const = const and numbers[i] == numbers[i - 1]
        asc = asc and numbers[i] > numbers[i - 1]
        weak_asc = weak_asc and numbers[i] >= numbers[i - 1]
        desc = desc and numbers[i] < numbers[i - 1]
        weak_desc = weak_desc and numbers[i] <= numbers[i - 1]
    return const, asc, weak_asc, desc, weak_desc


def main():
    numbers = get_list()
    const, asc, weak_asc, desc, weak_desc = check_list(numbers)
    if const:
        print('CONSTANT')
    elif asc:
        print('ASCENDING')
    elif weak_asc:
        print('WEAKLY ASCENDING')
    elif desc:
        print('DESCENDING')
    elif weak_desc:
        print('WEAKLY DESCENDING')
    else:
        print('RANDOM')


if __name__ == '__main__':
    main()

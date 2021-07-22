from collections import defaultdict


def accounts(trans):
    clients_dict = defaultdict(int)
    for tran in trans:
        if tran[0] == 'DEPOSIT':
            clients_dict[tran[1]] += int(tran[2])
        elif tran[0] == 'WITHDRAW':
            clients_dict[tran[1]] -= int(tran[2])
        elif tran[0] == 'BALANCE':
            if tran[1] not in clients_dict:
                print('ERROR')
            else:
                print(clients_dict[tran[1]])
        elif tran[0] == 'TRANSFER':
            clients_dict[tran[1]] -= int(tran[3])
            clients_dict[tran[2]] += int(tran[3])
        elif tran[0] == 'INCOME':
            for key in clients_dict.keys():
                if clients_dict[key] > 0:
                    clients_dict[key] += int(clients_dict[key]
                                             * int(tran[1]) / 100)
                else:
                    pass


def main():
    with open('input.txt', 'r') as file:
        trans = list(map(lambda line: line.split(), file.readlines()))
        accounts(trans)


if __name__ == '__main__':
    main()

def similar_genomes(genome_1, genome_2):
    set_genomes = set()

    for i in range(len(genome_2) - 1):
        set_genomes.add(genome_2[i:i + 2])

    answer = 0
    for i in range(len(genome_1) - 1):
        if genome_1[i:i + 2] in set_genomes:
            answer += 1

    return answer


def main():
    print(similar_genomes(input(), input()))


if __name__ == '__main__':
    main()

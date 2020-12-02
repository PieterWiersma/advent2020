
from itertools import combinations
from functools import reduce
import argparse

def find_numbers(number_to_find, list_of_numbers, no_of_entries):
    for combination in combinations(list_of_numbers, no_of_entries):
        if sum(combination) == number_to_find:
            return combination


def read_input(location):
    l = []
    with open(location) as f:
        for line in f:
            l.append(int(line))
    return l


def multiplier(t):
    return reduce((lambda x, y: x * y), t)


def main(args):
    input = read_input(args.inputfile)
    output = find_numbers(args.number_to_find, input, args.no_entries)
    print(multiplier(output))


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputfile', type=str)
    parser.add_argument('--no_entries', type=int)
    parser.add_argument('--number_to_find', type=int)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = cli()
    main(args)

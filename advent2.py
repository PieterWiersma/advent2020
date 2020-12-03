

import argparse


def read_input(location):
    l = []
    with open(location) as f:
        for line in f:
            l.append(line.strip())
    return l


def split_input(s):
    l = s.split(' ')
    min_max = [int(x) for x in l[0].split('-')]
    required_letter =l[1][:1]
    password = l[2]
    return min_max, required_letter, password


def check_condition_1(min_max, required_letter, password):
    no_of_occurences = password.count(required_letter)
    return min_max[0] <= no_of_occurences <= min_max[1]


def check_condition_2(min_max, required_letter, password):
    check_1 = password[min_max[0]-1] == required_letter
    check_2 = password[min_max[1]-1] == required_letter
    return int(check_1) + int(check_2) == 1


def main(args):
    input = read_input(args.inputfile)
    counter = 0
    for line in input:
        min_max, required_letter, password = split_input(line)
        counter += int(check_condition_2(min_max, required_letter, password))
    print(counter)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputfile', type=str)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = cli()
    main(args)

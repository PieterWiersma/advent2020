

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
    return (min_max, required_letter, password)


def check_condition_1(line):
    no_of_occurences = line[2].count(line[1])
    return line[0][0] <= no_of_occurences <= line[0][1]


def check_condition_2(line):
    check_1 = line[2][line[0][0]-1] == line[1]
    check_2 = line[2][line[0][1]-1] == line[1]
    return int(check_1) + int(check_2) == 1


def main(args):
    input = read_input(args.inputfile)
    input = [split_input(x) for x in input]
    counter = 0
    for line in input:
        counter = counter + int(check_condition_2(line))
    print(counter)

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputfile', type=str)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = cli()
    main(args)

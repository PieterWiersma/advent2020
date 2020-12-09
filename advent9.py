
from argparse import ArgumentParser, FileType
from itertools import combinations



def assignment_1(args):
    lines = [int(x.strip()) for x in args.inputfile]
    for i, value in enumerate(lines):
        check = False
        if i > args.preamble:
            for combination in combinations(lines[i-args.preamble:i], 2):
                if sum(combination) == value:
                    check = True
            if not check:
                return value, lines, args.preamble


def assignment_2(value, lines, preamble):
    lines = lines[:lines.index(value)]
    for i in range(len(lines)):
        for j in range(len(lines)-1, i, -1):
            if sum(lines[i:j]) == value:
                print(min(lines[i:j]) + max(lines[i:j]) )


def cli():
    parser = ArgumentParser()
    parser.add_argument('--inputfile', type=FileType("r"))
    parser.add_argument('--preamble', type=int)
    args = parser.parse_args()
    return args


a,b,c = assignment_1(cli())
assignment_2(a, b, c)

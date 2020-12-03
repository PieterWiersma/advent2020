
from argparse import ArgumentParser, FileType

def multiplier(t):
    return reduce((lambda x, y: x * y), t)


def move(inputfile, tree, steps):
    length_hor = len(inputfile[0])
    length_vert = len(inputfile)
    position = (0,0)
    counter = 0
    while (position[1] < length_vert-1):
        position = [x + y for x, y in zip(position, steps)]
        check = inputfile[position[1]][position[0] % length_hor]
        counter = counter + int(check == tree)
    return counter


def main(args):
    inputfile = [x.strip() for x in args.inputfile]
    steps = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    lis = []
    for step in steps:
        lis.append(move(inputfile, '#', step))
    print(multiplier(lis))

def cli():
    parser = ArgumentParser()
    parser.add_argument('--inputfile', type=FileType("r"))
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = cli()
    main(args)

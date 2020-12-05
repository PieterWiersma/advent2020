

from argparse import ArgumentParser, FileType
from math import floor


def command_splitter(command):
    bf_chars = command[:7]
    rl_chars = command[7:]
    return bf_chars, rl_chars


def half_stepper(bf_range, command):
    steps = bf_range[1] - bf_range[0]
    if command in ('F', 'L'):
        bf_range[1] = bf_range[1] - steps / 2
    elif command in ('B', 'R'):
        bf_range[0] = bf_range[0] + steps / 2

    return [floor(bf_range[0]), floor(bf_range[1])]


def get_seat(command):
    bf_range = [0, 127]
    rl_range = [0, 7]
    bf_chars, rl_chars = command_splitter(command)

    for command in bf_chars:
        bf_range = half_stepper(bf_range, command)
    bf_seat = bf_range[1]

    for command in rl_chars:
        rl_range = half_stepper(rl_range, command)
    rl_seat = rl_range[1]

    id = bf_seat * 8 + rl_seat
    print('row %s, column %s, id %s' % (bf_seat, rl_seat, id))
    return id


def find_seat(ids):
    seats = range(min(ids), max(ids))
    missing_seats = [x for x in seats if x not in ids]
    return missing_seats


def main(args):
    commands = [x.strip() for x in args.inputfile]
    ids = []
    for command in commands:
        ids.append(get_seat(command))

    print('max id %s' % max(ids) )
    print('seats not filled: %s' % find_seat(ids))


def cli():
    parser = ArgumentParser()
    parser.add_argument('--inputfile', type=FileType("r"))
    args = parser.parse_args()
    return args

args = cli()
main(args)



from argparse import ArgumentParser, FileType
from math import floor


def command_splitter(command):
    bf_chars = command[:7]
    rl_chars = command[7:]
    return bf_chars, rl_chars


def get_seat_id(command):
    bf_chars, rl_chars = command_splitter(command)
    bf_seat = int(bf_chars.replace("B", "1").replace("F", "0"), 2)
    rl_seat = int(rl_chars.replace("R", "1").replace("L", "0"), 2)

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
        ids.append(get_seat_id(command))

    print('max id %s' % max(ids) )
    print('seats not filled: %s' % find_seat(ids))


def cli():
    parser = ArgumentParser()
    parser.add_argument('--inputfile', type=FileType("r"))
    args = parser.parse_args()
    return args

args = cli()
main(args)

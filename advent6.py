
from argparse import ArgumentParser, FileType


def create_input(inputfile):
    container = []
    tmp_str = ''
    for line in inputfile:
        line = line.strip('\n')
        if line:
            tmp_str += '' + line
        else:
            container.append(tmp_str)
            tmp_str = ''
    container.append(tmp_str)

    return container


def how_many_answered(answers):
    return len(set([x for x in answers]))

def assignment_1(args):
    answers = create_input_2(args.inputfile)
    import pdb; pdb.set_trace()
    l = []
    for answer in answers:
        l.append(how_many_answered(answer))
    print(sum)


def create_input_2(inputfile):
    container = []
    tmp_str = []
    for line in inputfile:
        line = line.strip('\n')
        if line:
            tmp_str.append(line)
        else:
            container.append(tmp_str)
            tmp_str = []
    container.append(tmp_str)

    return container


def how_many_all_answered(answers):
    tmp_set = set([x for x in answers[0]])
    if len(answers)  > 1:
        for answer in answers[1:]:
            tmp_set = tmp_set & set([x for x in answer])
    return len(tmp_set)


def assignment_2(args):
    answers = create_input_2(args.inputfile)
    l = []
    for answer in answers:
        l.append(how_many_all_answered(answer))
    print(sum(l))



def cli():
    parser = ArgumentParser()
    parser.add_argument('--inputfile', type=FileType("r"))
    args = parser.parse_args()
    return args

args = cli()
assignment_2(args)

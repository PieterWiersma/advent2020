
from argparse import ArgumentParser, FileType

import re

def create_input(inputfile):
    """
    The way this works, you need to add an extra line to the inputfile with like an 'x'
    """

    container = []
    tmp_str = ''
    for line in inputfile:
        line = line.strip('\n')
        if line:
            tmp_str += ' ' + line
        else:
            container.append(tmp_str)
            tmp_str = ''
    return container


def check_assignment_1(input_str, requirements, trailing_char):
    checksum = 0
    for key in requirements.keys():
        if input_str.find(key + trailing_char) + 1:
            checksum += requirements[key]
    #print('checksum %s, line: %s' % (checksum, input_str))
    return int(checksum == sum(requirements.values()))



def assignment_1(args):
    input = create_input(args.inputfile)
    requirements = {"byr":1,
                    "iyr":1,
                    "eyr":1,
                    "hgt":1,
                    "hcl":1,
                    "ecl":1,
                    "pid":1,
                    "cid":0 }

    counter = 0
    for line in input:
        counter += check_assignment_1(line, requirements, ':')
    print('%s passport valid' % counter)



def check_assignment_2(input_str, requirements):
    checksum = 0
    for key in requirements.keys():
        funct_output = input_str
        for func in requirements[key]:
            if funct_output:
                funct_output = func(funct_output)
        if funct_output:
            checksum += 1
    #if checksum == 6: print('checksum %s input: %s \n\n ' % (checksum, input_str))
    return int(checksum == len(requirements))


def assignment_2(args):
    input = create_input(args.inputfile)
    requirements = {"byr": [(lambda x: re.findall('byr:(\d{4})', x)),
                            (lambda x: 1920 <= int(x[0]) <= 2002)],
                    "iyr":[(lambda x: re.findall('iyr:(\d{4})', x)),
                            (lambda x: 2010 <= int(x[0]) <= 2020)],
                    "eyr":[(lambda x: re.findall('eyr:(\d{4})', x)),
                            (lambda x: 2020 <= int(x[0]) <= 2030)],
                    "hgt":[(lambda x: re.findall('hgt:(\d{2,3})(in|cm)', x)),
                            (lambda x: 150 <= int(x[0][0]) <= 193 if x[0][1] == 'cm' else 59 <= int(x[0][0]) <= 76 )],
                    "hcl":[lambda x: re.findall('hcl:#([0-9a-f]{6})', x)],
                    "ecl":[(lambda x: re.findall('ecl:(\w{3})', x)),
                            (lambda x: x[0] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])],
                    "pid":[(lambda x: re.findall('pid:(\d{9})(?:\D|$)', x))]
                    }
    counter = 0
    for line in input:
        counter += check_assignment_2(line, requirements)
    print('%s passport valid' % counter)


def cli():
    parser = ArgumentParser()
    parser.add_argument('--inputfile', type=FileType("r"))
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = cli()
    #assignment_1(args)
    assignment_2(args)

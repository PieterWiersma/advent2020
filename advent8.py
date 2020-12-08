
from argparse import ArgumentParser, FileType

import copy

class Computer:
    def __init__(self):
        self.history = []
        self.step = 0
        self.acc_score = 0

    def nop(self, instruction):
        self.history.append(self.step)
        self.step += 1

    def acc(self, instruction):
        self.history.append(self.step)
        self.step += 1
        self.acc_score += instruction

    def jmp(self, instruction):
        self.history.append(self.step)
        if instruction == 0:
            self.step += 1
        else:
            self.step += instruction



def create_instructions(inputfile):
    l = []
    for line in inputfile:
        tmp_l = line.strip().split(' ')
        l.append({
            "name": tmp_l[0],
            "instr": 0 + int(tmp_l[1])
        })
    return l


def assignment_1(args):
    instructions = create_instructions(args.inputfile)
    computer = Computer()
    nops_and_jumps = []
    changed_instructions = []
    original = copy.deepcopy(instructions)

    for i, item in enumerate(original):
        while 1:
            instruction = instructions[computer.step]
            if instruction['name'] == 'nop':
                computer.nop(instruction['instr'])
            elif instruction['name'] == 'jmp':
                computer.jmp(instruction['instr'])
            elif instruction['name'] == 'acc':
                computer.acc(instruction['instr'])

            if computer.step in computer.history:
                break;

            if computer.step >= len(instructions):
                print(computer.acc_score)
                return

        instructions = copy.deepcopy(original)
        if item['name'] == 'nop':
            instructions[i]['name'] = 'jmp'
        if item['name'] == 'jmp':
            instructions[i]['name'] = 'nop'
        computer = Computer()

    print(computer.acc_score)





def cli():
    parser = ArgumentParser()
    parser.add_argument('--inputfile', type=FileType("r"))
    args = parser.parse_args()
    return args



assignment_1(cli())


from argparse import ArgumentParser, FileType
import re

PARENT_BAG_RE = re.compile('^(.*?)bags contain')
CHILD_BAG_RE = re.compile('(?:contain|,) (\d{1,2})([a-zA-Z0-9_ ]*) (?:.|,)')

def create_dataset(lines):
    container = {}
    for line in lines:
        parent = PARENT_BAG_RE.findall(line)[0].strip()
        container[parent] = []
        for item in CHILD_BAG_RE.findall(line):
            container[parent].append((int(item[0]), item[1].strip()))
    return container


def look_for_value(dataset, search_bag):
    found_bags = []
    for key, values in dataset.items():
        for value in values:
            if value[1] == search_bag:
                found_bags.append(key)
    return found_bags, value[0]


def recursive_product_seeker(dataset, search_bag):
    l = []
    for item in dataset[search_bag]:
        if dataset[item[1]]:
            l.append(item[0] * recursive_product_seeker(dataset, item[1]) + item[0])
        else:
            l.append(item[0])
    return sum(l)


def assignment_1(args):
    search_bag = 'shiny gold'
    lines = [x.strip() for x in args.inputfile]
    dataset = create_dataset(lines)
    search_for_bags = [search_bag]
    bags_with_search_bag = []
    while search_for_bags:
        total_results = []
        for bag in search_for_bags:
            results, _ = look_for_value(dataset, bag)
            bags_with_search_bag = list(set(bags_with_search_bag + results))
            total_results = total_results + results

        if not total_results:
            break
        search_for_bags = total_results

    print(len(bags_with_search_bag))



def assignment_2(args):
    search_bag = 'shiny gold'
    lines = [x.strip() for x in args.inputfile]
    dataset = create_dataset(lines)
    outcome = recursive_product_seeker(dataset, search_bag)
    print(outcome)

    #print(test)

def cli():
    parser = ArgumentParser()
    parser.add_argument('--inputfile', type=FileType("r"))
    args = parser.parse_args()
    return args



assignment_2(cli())

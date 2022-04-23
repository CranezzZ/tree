import random
from typing import List

from numpy import ones_like

def generate_txt_sample(args):
    random_i = random.randint(2, 4)
    with open(args.tree_path, 'w') as wf:
        wf.write('root\n')
        for i in range(random_i):
            wf.write(args.special_symbol + str(i) + '\n')
            random_j = random.randint(2, 4)
            for j in range(random_j):
                wf.write(args.special_symbol * 2 + str(i) + str(j) + '\n')
                random_k = random.randint(2, 4)
                for k in range(random_k):
                    wf.write(args.special_symbol * 3 + str(i) + str(j) + str(k) + '\n')


def get_tree_txt_lines(args) -> List:
    retList = list()
    with open(args.tree_path, 'r') as rf:
        lines = rf.readlines()
    for line in lines:
        oneLine = [-1, ""]
        oneLine[0] = get_ident(args, line)
        oneLine[1] = line.strip().strip(args.special_symbol)
        retList.append(oneLine)
        #print(oneLine)
    #print(retList)
    return retList



def get_ident(args, s: str) -> int:
    for i, c in enumerate(s):
        if c != args.special_symbol:
            break
    return i

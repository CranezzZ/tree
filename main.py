'''
Author: Crane
Date: 2022-04-23 00:46:31
LastEditors: Crane
LastEditTime: 2022-04-23 10:40:51
FilePath: /Tree/tree/main.py
Description: Entry for program runtime

email: crane@buaa.edu.cn
'''

from os import system
from sklearn import tree
from args import get_args
import utils
from systemTree import Tree, TreeNode
def debug(args):
    # utils.generate_txt_sample(args)
    # linesList = utils.get_tree_txt_lines(args)
    systemTree = Tree(args)
    rootNode = systemTree.init_requirement_tree(args)
    #rootNode.dfs()
    systemTree.set_leaf_nodes()

if __name__ == '__main__':
    args = get_args()
    debug(args=args)
'''
Author: Crane
Date: 2022-04-23 10:45:43
LastEditors: Crane
LastEditTime: 2022-04-23 11:00:30
FilePath: /Tree/tree/systemTree.py
Description: the definition of the requirement system tree

email: crane@buaa.edu.cn
'''

class TreeNode():
    def __init__(self, args) -> None:
        self.parent = None
        self.children = list()
        self.represention = None
        self.isLeaf = False

class Tree():
    def __init__(self, args) -> None:
        self.root = None
        self.leafNodes = list()
        
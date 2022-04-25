'''
Author: Crane
Date: 2022-04-23 10:45:43
LastEditors: Crane
LastEditTime: 2022-04-23 11:00:30
FilePath: /Tree/tree/systemTree.py
Description: the definition of the requirement system tree

email: crane@buaa.edu.cn
'''

from codecs import getreader
from utils import get_tree_txt_lines, get_representation
from transformers import BertTokenizer, AlbertModel

class TreeNode():
    def __init__(self, init_text, depth=-1) -> None:
        self.parent = None
        self.children = list()
        self.represention = None
        self.isLeaf = False
        self.text = init_text
        self.depth = depth
        
    
    def get_depth(self) -> int:
        return self.depth

    def dfs(self) -> None:
        if self is None:
            return
        print(self.text)
        for _, item in enumerate(self.children):
            item.dfs()
        

class Tree():
    def __init__(self, args) -> None:
        self.root = None
        self.leafNodes = list()
        self.leafRepres = list()

    def init_requirement_tree(self, args) -> TreeNode:
        linesList = get_tree_txt_lines(args)
        linesListLength = len(linesList)
        if linesListLength == 0 or linesList[0][0] != 0:
            raise ValueError('Illegal input file, plz check!')
        root = TreeNode(linesList[0][1], linesList[0][0])
        cur = root
        for i in range(1, linesListLength):
            depth = linesList[i][0]
            text = linesList[i][1]
            tempNode = TreeNode(text, depth)
            if depth == cur.depth + 1:
                cur.children.append(tempNode)
                tempNode.parent = cur
                cur = tempNode
            elif depth == cur.depth:
                cur = cur.parent
                cur.children.append(tempNode)
                tempNode.parent = cur
                cur = tempNode
            else:
                for i in range(cur.depth - depth + 1):
                    cur = cur.parent
                cur.children.append(tempNode)
                tempNode.parent = cur
                cur = tempNode
        self.root = root
        return self.root

    def set_leaf_nodes(self) -> None:
        stk = [self.root]
        while len(stk) > 0:
            cur = stk.pop(0)
            if len(cur.children) == 0:
                self.leafNodes.append(cur)
            else:
                stk.extend(cur.children)
        for item in self.leafNodes:
            print(item.text)
        
    def init_leaf_nodes_repre(self, model_path, tokenizer_path) -> None:
        tokenizer = BertTokenizer.from_pretrained(tokenizer_path)
        albert = AlbertModel.from_pretrained(model_path)
        self.leafRepres = [get_representation(item.text, tokenizer, albert) for item in self.leafNodes]
        print(len(self.leafNodes), len(self.leafRepres))
        print(self.leafRepres)
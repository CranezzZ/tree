'''
Author: Crane
Date: 2022-04-23 10:41:03
LastEditors: Crane
LastEditTime: 2022-04-23 10:41:03
FilePath: /Tree/tree/args.py
Description: parser initial

email: crane@buaa.edu.cn
'''

import argparse

def get_args():
    parser = argparse.ArgumentParser(description='parser')
    parser.add_argument('--tree_path', type=str, default='test.txt', help='the initial txt path of the requirement system tree')
    parser.add_argument('--special_symbol', type=str, default='$', help='the special symbol of the prefix of lines in the tree text file')
    parser.add_argument('--tokenizer_path', type=str, default="clue/albert_chinese_tiny", help='')
    parser.add_argument('--model_path', type=str, default="clue/albert_chinese_tiny", help='')
    args = parser.parse_args()
    return args
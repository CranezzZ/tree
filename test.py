# import paddlehub as hub

# # Load ernie pretrained model
# module = hub.Module(name="ernie_tiny")
# module.
# inputs, outputs, program = module.context(trainable=True, max_seq_len=128)

# # Must feed all the tensor of ernie's module need
# input_ids = inputs["input_ids"]
# position_ids = inputs["position_ids"]
# segment_ids = inputs["segment_ids"]
# input_mask = inputs["input_mask"]

# # Use "pooled_output" for sentence-level output.
# pooled_output = outputs["pooled_output"]

# # Use "sequence_output" for token-level output.
# sequence_output = outputs["sequence_output"]
# Downloading ernie_tiny.pdparams from https://bj.bcebos.com/paddlenlp/models/transformers/ernie_tiny/ernie_tiny.pdparams
# (paddle) C:\Users\11847>hub install ernie_tiny==2.0.2
# C:\Users\11847\anaconda3\envs\paddle\lib\site-packages\paddle\vision\transforms\functional_pil.py:36: DeprecationWarning: NEAREST is deprecated and will be removed in Pillow 10 (2023-07-01). Use Resampling.NEAREST or Dither.NONE instead.
#   'nearest': Image.NEAREST,
# C:\Users\11847\anaconda3\envs\paddle\lib\site-packages\paddle\vision\transforms\functional_pil.py:37: DeprecationWarning: BILINEAR is deprecated and will be removed in Pillow 10 (2023-07-01). Use Resampling.BILINEAR instead.
#   'bilinear': Image.BILINEAR,
# C:\Users\11847\anaconda3\envs\paddle\lib\site-packages\paddle\vision\transforms\functional_pil.py:38: DeprecationWarning: BICUBIC is deprecated and will be removed in Pillow 10 (2023-07-01). Use Resampling.BICUBIC instead.
#   'bicubic': Image.BICUBIC,
# C:\Users\11847\anaconda3\envs\paddle\lib\site-packages\paddle\vision\transforms\functional_pil.py:39: DeprecationWarning: BOX is deprecated and will be removed in Pillow 10 (2023-07-01). Use Resampling.BOX instead.
#   'box': Image.BOX,
# C:\Users\11847\anaconda3\envs\paddle\lib\site-packages\paddle\vision\transforms\functional_pil.py:40: DeprecationWarning: LANCZOS is deprecated and will be removed in Pillow 10 (2023-07-01). Use Resampling.LANCZOS instead.
#   'lanczos': Image.LANCZOS,
# C:\Users\11847\anaconda3\envs\paddle\lib\site-packages\paddle\vision\transforms\functional_pil.py:41: DeprecationWarning: HAMMING is deprecated and will be removed in Pillow 10 (2023-07-01). Use Resampling.HAMMING instead.
#   'hamming': Image.HAMMING
# Download https://bj.bcebos.com/paddlehub/paddlehub_dev/ernie_tiny.zip
# [##################################################] 100.00%
# Decompress C:\Users\11847\.paddlehub\tmp\tmphn0373ir\ernie_tiny.zip
# [##################################################] 100.00%
# [2022-04-23 22:14:48,373] [    INFO] - Successfully installed ernie_tiny-2.0.2

from codecs import getreader
from sympy import sequence
import torch
from transformers import BertTokenizer, AlbertModel
import numpy as np


def cos_sim(vector_a, vector_b):
    """
    计算两个向量之间的余弦相似度
    :param vector_a: 向量 a 
    :param vector_b: 向量 b
    :return: sim
    """
    vector_a = np.mat(vector_a)
    vector_b = np.mat(vector_b)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim





def get_representation(s: str, tokenizer, model):
    inputs = tokenizer(s, return_tensors="pt")
    outputs = model(**inputs).pooler_output.squeeze(0).tolist()
    #print(outputs.shape)
    # outputs = albert(**inputs).last_hidden_state[:, 0, :].squeeze(0).tolist()
    #outputs = [1]
    return outputs

if __name__ == '__main__':
    tokenizer = BertTokenizer.from_pretrained("clue/albert_chinese_tiny")
    albert = AlbertModel.from_pretrained("clue/albert_chinese_tiny")
    llist = ['武器装备武器装备', '武器装备', '一二三四五六七一二三四五六七一二三四五六七一二三四五六七一二三四五六七一二三四五六七']
    n = len(llist)
    repres = [get_representation(item, tokenizer, albert) for item in llist]
    for i in range(n - 1):
        for j in range(i + 1, n):
            print(cos_sim(repres[i], repres[j]))

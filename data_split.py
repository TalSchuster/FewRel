import os
import random
from shutil import copyfile
import json

random.seed(123)

ROOT_PATH = './data/'

k = 5
target_path = './data/wiki_5_splits/'

'''
Splits the training set to 5 folds.
In each split, the held out set is used for test.
'''

path = os.path.join(ROOT_PATH, 'train_wiki' + '.json')
data = json.load(open(path, 'r'))
relations = list(data.keys())
num_relations = len(relations)

rels_per_split = round(num_relations / k)

random.shuffle(relations)

for i in range(k):
    split_val_rels = relations[i*rels_per_split: (i+1)*rels_per_split]

    split_train = {}
    split_val = {}
    for rel, examples in data.items():
        if rel in split_val_rels:
            split_val[rel] = examples
        else:
            split_train[rel] = examples

    print(f"split {i}: train: {len(split_val.keys())}, test: {len(split_train.keys())}")

    os.makedirs(os.path.join(target_path, str(i)), exist_ok=True)
    with open(os.path.join(target_path, str(i), 'train.json'), 'w') as f:
        json.dump(split_train, f)
    with open(os.path.join(target_path, str(i), 'val.json'), 'w') as f:
        json.dump(split_val, f)

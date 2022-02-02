# coding: utf-8

import json
import os
import pprint
from collections import OrderedDict

root_path = os.path.dirname(os.path.abspath(__file__))
json_file3 = os.path.join(root_path, 'data', 'thirukkural_meanings.json')
json_file1 = os.path.join(root_path, 'data', 'thirukural_git.json')
json_file2 = os.path.join(root_path, 'data', 'thirukkural.json')

with open(json_file3, encoding='utf-8') as fp:
    t3 = json.load(fp)
with open(json_file1, encoding='utf-8') as fp:
    t1 = json.load(fp)
with open(json_file2, encoding='utf-8') as fp:
    t2 = json.load(fp)

# print(t.keys(), len(t.keys()))

print(t1.keys(), len(t1["kurals"]))

print(t2.keys(), len(t2["kural"]))

#  t1 + t2
t12 = OrderedDict()

for value in t1["kurals"] + t2["kural"]:
    if "number" in value.keys():
        kural_number = value["number"]
    else:
        kural_number = value["Number"]
    if kural_number not in t12.keys():
        t12[kural_number] = OrderedDict()
        t12[kural_number] = value
    else:
        t12[kural_number].update(**value)

pprint.pprint(t12[1])
print(t12[1].keys())

t12_new = dict()

move_keys = {
    "kural": ['kural', 'Line1', 'Line2', 'transliteration1', 'transliteration2'],
    "chapter": ['adikaram_name', 'adikaram_transliteration', 'adikaram_translation'],
    "section": ['paul_name', 'paul_transliteration', 'paul_translation'],
    "type": ['iyal_name', 'iyal_transliteration', 'iyal_translation'],
    "meaning": ["meaning", 'Translation', 'couplet', 'mk'],
}
for kural, data in t12.items():
    t12_new[kural] = dict()
    temp = t12_new[kural]
    for k1, v1 in move_keys.items():
        temp[k1] = dict()
        for _v1 in v1:
            if isinstance(data[_v1], dict):
                temp[k1].update(**data[_v1])
            else:
                temp[k1][_v1] = data[_v1]

pprint.pprint(t12_new[1])
print(t12_new[1].keys())

print(len(t12_new))

for kural in t3.keys():
    meaning = dict()
    x = t3[kural]
    x.pop("translation")
    x.pop("explanation")
    meaning.update(**x)
    meaning["explanation"] = t12_new[int(kural)]["meaning"]["en"]
    meaning["translation"] = t12_new[int(kural)]["meaning"]["Translation"]
    meaning["couplet"] = t12_new[int(kural)]["meaning"]["couplet"]
    t12_new[int(kural)]["meaning"] = meaning

output = 'thirukkural_metadata.json'

with open(output, 'w', encoding='utf-8') as fp:
    json.dump(t12_new, fp, ensure_ascii=False, indent=4)

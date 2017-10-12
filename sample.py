import json
import os
import pprint
import random

json_file = 'all_thirukkural_information.json'
json_file1 = 'thirukural_git.json'


if os.path.isfile(json_file):
    with open(json_file) as fp:
        thirukkural = json.load(fp, encoding='utf-8')
    with open(json_file1) as fp:
        thirukkural1 = json.load(fp, encoding='utf-8')
else:
    print('File not found')
    exit()

template = """
குறள் எண்: {number} \n
அதிகாரம்: {chapter} ({chapter_ta} - {chapter_en})\n
குறள் பால்: {section} ({section_ta} - {section_en})\n
குறள் இயல்: {iyal} ({iyal_ta} - {iyal_en})\n
குறள் - {kural} \n
குறள் விளக்கம்:\n{ta_meaning}\n

transliteration: {transliteration}\n 
couplet: {couplet}\n
translation: {translation}\n
explanation: {en_meaning}\n
"""

all_kural = []
# key = random.randrange(1331)
for key in range(1331):
    try:
        sample1 = thirukkural1['kurals'][key]
        # pprint.pprint(sample1)
        sample = thirukkural[str(key+1)]
        # pprint.pprint(sample)

        section = sample1['section']
        chapter = sample1['chapter']
        kural = '\n       '.join(sample1['kural'])
        number = sample1['number']
        ta_meaning = '\n'.join([sample1['meaning']['ta_salamon'], sample1['meaning']['ta_mu_va']])
        en_meaning = sample1['meaning']['en']
        couplet = sample['1_couplet']
        transliteration = '\n\t\t\t\t '.join([sample['1_transliteration1'], sample['1_transliteration2']])
        translation = sample['1_translation']
        iyal = sample['3_pal']
        iyal_en = sample['3_translation']
        chapter_en  = sample['2_translation']
        section_en = sample['4_translation']
        iyal_ta = sample['3_transliteration']
        chapter_ta  = sample['2_transliteration']
        section_ta = sample['4_transliteration']
        all_kural.append(template.format(chapter=chapter, section=section, kural=kural, section_en=section_en,
                   number=number, ta_meaning=ta_meaning, iyal=iyal,iyal_en=iyal_en,
                   en_meaning=en_meaning, couplet=couplet,chapter_en=chapter_en,
                   transliteration=transliteration, translation=translation,
                   iyal_ta=iyal_ta, chapter_ta=chapter_ta, section_ta=section_ta))
    except:
        print('Error ', key)


output = 'all_kural.json'
#
# with open(output, 'w') as fp:
#     json.dump(all_kural, fp, ensure_ascii=False, indent=4)
#
# print(len(all_kural))

with open(output) as fp:
    thirukkural = json.load(fp, encoding='utf-8')

# key = random.randrange(1331)

for key in range(1330):
    if key in [394, 647]:
        print(thirukkural[key])
        print('-'*120)

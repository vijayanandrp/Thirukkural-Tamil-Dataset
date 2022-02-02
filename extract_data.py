import os

file2_path = r'C:\Users\hai\Documents\GitHub\Thirukkural-Tamil-Dataset\data\text_all'

import re
import json

t3 = dict()

for file1 in os.listdir(file2_path):
    print("==========>>>>>>", file1)
    text1 = " ".join(open(os.path.join(file2_path, file1), encoding='utf-8').readlines())
    text1 = text1.replace("\n", "").replace("\r", "").replace('\xa0', '')
    text1 = re.sub(' +', ' ', text1)
    kurals = re.findall(r"குறள்\s(\d+):(.*?)மேலே செல்ல", text1)
    for kural in kurals:
        try:
            print("========")
            print("Kural ", kural[0])
            mu_karunanidhi = re.search("(கலைஞர் மு.கருணாநிதி உரை:.*)மு.வரதராசனார் உரை:", kural[1]).group(1)
            print("mu_karunanidhi ", mu_karunanidhi.strip())
            mu_varadha = re.search("(மு.வரதராசனார் உரை:.*)சாலமன் பாப்பையா உரை:", kural[1]).group(1)
            print("mu_varadha ", mu_varadha.strip())
            salaman_papa = re.search("(சாலமன் பாப்பையா உரை:.*)பரிமேலழகர் உரை:", kural[1]).group(1)
            print("salaman_papa ", salaman_papa.strip())
            pari_melakar = re.search("(பரிமேலழகர் உரை:.*)மணக்குடவர் உரை:", kural[1]).group(1)
            print("pari_melakar ", pari_melakar.strip())
            v_munusami = ""
            if "திருக்குறளார் வீ. முனிசாமி உரை:" in kural[1]:
                mani_kudavar = re.search("(மணக்குடவர் உரை:.*)திருக்குறளார் வீ. முனிசாமி உரை:", kural[1]).group(1)
                print("mani_kudavar ", mani_kudavar.strip())
                v_munusami = re.search("(திருக்குறளார் வீ. முனிசாமி உரை:.*)Translation:", kural[1]).group(1)
                print("v_munusami ", v_munusami.strip())
            else:
                mani_kudavar = re.search("(மணக்குடவர் உரை:.*)Translation:", kural[1]).group(1)
                print("mani_kudavar ", mani_kudavar.strip())
            translation = re.search("Translation:(.*)Explanation:", kural[1]).group(1)
            print("Translation ", translation.strip())
            explanation = re.search("Explanation:(.*)", kural[1]).group(1)
            print("Explanation ", explanation.strip())
            if kural not in t3.keys():
                t3[kural[0]] = dict()
                t3[kural[0]]["mu_karunanidhi"] = mu_karunanidhi
                t3[kural[0]]["mu_varadha"] = mu_varadha
                t3[kural[0]]["salaman_papa"] = salaman_papa
                t3[kural[0]]["pari_melakar"] = pari_melakar
                t3[kural[0]]["mani_kudavar"] = mani_kudavar
                t3[kural[0]]["v_munusami"] = v_munusami
                t3[kural[0]]["translation"] = translation
                t3[kural[0]]["explanation"] = explanation
            else:
                if not t3[kural[0]]["mu_karunanidhi"]:
                    t3[kural[0]]["mu_karunanidhi"] = mu_karunanidhi
                if not t3[kural[0]]["mu_varadha"]:
                    t3[kural[0]]["mu_varadha"] = mu_varadha
                if not t3[kural[0]]["salaman_papa"]:
                    t3[kural[0]]["salaman_papa"] = salaman_papa
                if not t3[kural[0]]["pari_melakar"]:
                    t3[kural[0]]["pari_melakar"] = pari_melakar
                if not t3[kural[0]]["mani_kudavar"]:
                    t3[kural[0]]["mani_kudavar"] = mani_kudavar
                if not t3[kural[0]]["v_munusami"]:
                    t3[kural[0]]["v_munusami"] = v_munusami
                if not t3[kural[0]]["translation"]:
                    t3[kural[0]]["translation"] = translation
                if not t3[kural[0]]["explanation"]:
                    t3[kural[0]]["explanation"] = explanation

        except Exception as err:
            print(err)
            print(kural)
            print(os.path.join(file2_path, file1))
            raise

output = 'thirukkural_meanings.json'
with open(output, 'w', encoding='utf-8') as fp:
    json.dump(t3, fp, ensure_ascii=False, indent=4)

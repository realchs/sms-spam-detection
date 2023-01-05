import json
import pandas as pd

def exchange(num):

    num_json = str(num) +'.json'
    num_csv = "test_" + str(num) +".csv"
    #파일명

    with open(num_json, 'r', encoding='UTF-8') as file:
        datas = json.load(file)
        json_test = datas['data']
        #불러옴

        type_ = []
        topic_ = []
        utterance_ = []
        #초기화

        for k in json_test :
            try:
                t = k['header']['dialogueInfo']
                j = k['body']
                for i in j:
                    type_.append(t['type'])
                    topic_.append(t['topic'])
                    utterance_.append(i['utterance'])
            except:
                break
        #추출&누적

        df = pd.DataFrame(type_, columns = ['type'])
        df['topic'] = topic_
        df['utterance'] = utterance_
        df.to_csv(num_csv, index = False, encoding="utf-8-sig")
        #결과저장

#
for zzz in range(1,10):
    exchange(zzz)
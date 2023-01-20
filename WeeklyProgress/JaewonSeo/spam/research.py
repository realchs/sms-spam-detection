import os
import pandas as pd
import warnings
import re
import sys
from konlpy.tag import Okt
from collections import Counter
import konlpy

warnings.filterwarnings(action='ignore')

class research():
    def __init__(self):
         self.call_spam()
        # self.call_sms()

    def call_spam(self):
        file_format = "2022" # .csv .xlsx
        file_path = "./spam_data"
        file_list = [f"{file_path}/{file}" for file in os.listdir(file_path) if file_format in file]
        print(file_list)

        merge_df = pd.DataFrame()

        for file_name in file_list:
            file_df = pd.read_excel(file_name, engine="openpyxl", header=1)
            columns = ['신고유형', '스팸유형','회신번호','원발신번호', '메시지', '메시지 타입']
            temp_df = pd.DataFrame(file_df, columns=columns)
            merge_df = pd.concat([merge_df,temp_df])
        df_dic = merge_df.to_dict()
        arr1 = df_dic["회신번호"].values()
        arr2 = df_dic["원발신번호"].values()
        arr3 = df_dic["신고유형"].values()
        arr4 = df_dic["스팸유형"].values()
        arr5 = df_dic["메시지"].values()
        arr1_list = list(arr1) # 회신번호
        arr2_list = list(arr2) # 원발신번호
        arr3_list = list(arr3) # 신고유형
        arr4_list = list(arr4) # 스팸유형
        arr5_list = list(arr5) # 메시지
        print(arr1_list[0:3])
        print(arr2_list[0:3])

        #회신번호 분석
        counter = {}
        for ele in arr1_list:
            ele = str(ele)
            if ele in counter:
                counter[ele] += 1
            else:
                counter[ele] = 1
        dic1 = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))

        #원발신번호 분석
        counter = {}
        for ele in arr2_list:
            ele = str(ele)
            if ele in counter:
                counter[ele] += 1
            else:
                counter[ele] = 1
        dic2 = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))

        #신고유형 분석
        counter = {}
        for ele in arr3_list:
            ele = str(ele)
            if ele in counter:
                counter[ele] += 1
            else:
                counter[ele] = 1
        dic3 = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))

        #스팸유형 분석
        counter = {}
        for ele in arr4_list:
            ele = str(ele)
            if ele in counter:
                counter[ele] += 1
            else:
                counter[ele] = 1
        dic4 = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))

        # 내용 분석
        txt = ""
        for ele in arr5_list:
            ele = str(ele)
            if ele != "nan":
                txt += ele + "\n"


        konlpy.jvm.init_jvm(jvmpath=None, max_heap_size=1024*6)
        okt = Okt()
        noun = okt.nouns(txt)
        for i,v in enumerate(noun):
            if len(v)<2:
                noun.pop(i)

        count = Counter(noun)

        noun_list = count.most_common(100)

        #sys.stdout = open("out1.txt","w")
        #print(dic1)
        #sys.stdout.close()
        #sys.stdout = open("out2.txt","w")
        #print(dic2)
        #sys.stdout.close()
        #sys.stdout = open("out3.txt","w")
        #print(dic3)
        #sys.stdout.close()
        #sys.stdout = open("out4.txt","w")
        #print(dic4)
        #sys.stdout.close()
        sys.stdout = open("out5.txt","w")
        print(noun_list)
        sys.stdout.close()
        


        
        # merge_df.to_csv("merge.csv", index=False, encoding='utf-8-sig')
    
    def call_sms(self):
        file_df = pd.read_excel("sms_jw.xls", usecols=["address","body"])
        df_dic = file_df.to_dict()
        arr1 = df_dic["address"].values()
        arr2 = df_dic["body"].values()

        arr1_list = list(arr1) # 번호
        arr2_list = list(arr2) # 내용
        print(arr1_list[0:3])
        print(arr2_list[0:3])

        #번호 분석
        counter = {}
        for ele in arr1_list:
            ele = str(ele)
            if ele in counter:
                counter[ele] += 1
            else:
                counter[ele] = 1
        dic = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))
        #sys.stdout = open("addr.txt","w")
        #print(dic)
        #sys.stdout.close()

        # 내용 분석

        txt = ""
        for ele in arr2_list:
            ele = str(ele)
            if ele != "nan":
                txt += ele + "\n"


        okt = Okt()
        noun = okt.nouns(txt)
        for i,v in enumerate(noun):
            if len(v)<2:
                noun.pop(i)

        count = Counter(noun)

        noun_list = count.most_common(100)
        print(noun_list)

    # def split(self):
    #     total_file = "merge.csv"
    #     file_df = pd.read_excel(file_name)
    #     temp_df = pd.DataFrame(file_df, columns=nn)
    #     twt = Twitter()
    #     text = ''
    #     tagging = twt.pos(text)


if __name__=="__main__":
    research()
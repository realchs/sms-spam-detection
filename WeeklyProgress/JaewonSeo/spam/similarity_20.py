import os
import pandas as pd
import warnings
import re
import sys
from konlpy.tag import Okt
from collections import Counter
import konlpy
okt = Okt(max_heap_size= 1024 * 6)

warnings.filterwarnings(action='ignore')

class similarity():
    def call(self):
        # JW DATA part
        file_df1 = pd.read_excel("sms_jw.xls", usecols=["address","body"])
        df_dic1 = file_df1.to_dict()
        arr_jw = df_dic1["body"].values()
        arr_jw_list = list(arr_jw)
        txt_jw = ""
        for ele in arr_jw_list:
            ele = str(ele)
            if ele != "nan":
                txt_jw += ele + "\n"

        noun = okt.nouns(txt_jw)
        for i,v in enumerate(noun):
            if len(v)<2:
                noun.pop(i)
        
        count = Counter(noun)

        noun_list_jw = count.most_common(100)
        noun_list_jw = list(dict(noun_list_jw).keys())

        # SPAM DATA part

        file_format = "2022" # .csv .xlsx
        file_path = "./spam_data_test"
        file_list = [f"{file_path}/{file}" for file in os.listdir(file_path) if file_format in file]
        print(file_list)

        cnt = 0
        Jaccard_jw = []
        Jaccard_spam = []
        Cosine = []
        Euclidean = []
        for file_name in file_list:
            file_df = pd.read_excel(file_name, engine="openpyxl", header=1)
            columns = ['메시지']
            temp_df = pd.DataFrame(file_df, columns=columns)

            df_dic = temp_df.to_dict()
            arr = df_dic["메시지"].values()
            arr_list2 = list(arr) # 새파일 메시지
            
            txt = ""
            for ele in arr_list2:
                ele = str(ele)
                if ele != "nan":
                    txt += ele + "\n"

            #konlpy.jvm.init_jvm(jvmpath=None, max_heap_size=1024*6)
            
            noun = okt.nouns(txt)
            for i,v in enumerate(noun):
                if len(v)<2:
                    noun.pop(i)

            count = Counter(noun)

            noun_list2 = count.most_common(100) # 새파일 메시지 top100
            noun_list2 = list(dict(noun_list2).keys())
            
            #자카드 유사도_spam_mydata
            doc_union = set(noun_list_jw).union(set(noun_list2))
            doc_intersection = set(noun_list_jw).intersection(set(noun_list2))
            jaccard_similarity = len(doc_intersection) / len(doc_union)
            Jaccard_jw.append(jaccard_similarity)
            print("Jaccard_jw",cnt+1," : ",jaccard_similarity)
            
            if cnt != 0: # noun_list1 VS noun_list2
                #자카드 유사도_spam_spam
                doc_union = set(noun_list1).union(set(noun_list2))
                doc_intersection = set(noun_list1).intersection(set(noun_list2))
                jaccard_similarity = len(doc_intersection) / len(doc_union)
                Jaccard_spam.append(jaccard_similarity)
                print("Jaccard_spam",cnt," : ",jaccard_similarity)

                #코사인 유사도
                #유클리드 거리 개념

            noun_list1 = noun_list2
            cnt += 1
        
        mean1 = sum(Jaccard_jw)/len(Jaccard_jw)
        mean2 = sum(Jaccard_spam)/len(Jaccard_spam)
        # ouput, 평균 값
        Jaccard_out = open("Jaccard_out1.txt","w")

        for i1,v1 in enumerate(Jaccard_jw):
            Jaccard_out.write("Jaccard_jw{0} : {1}, ".format(i1,v1))
        Jaccard_out.write("\n\n")
        for i2,v2 in enumerate(Jaccard_spam):
            Jaccard_out.write("Jaccard_spam{0} : {1}, ".format(i2,v2))
        Jaccard_out.write("\n\n")
        Jaccard_out.write("Jaccard_jw mean : {0}, Jaccard_spam mean : {1}".format(mean1,mean2))

        Jaccard_out.close()


if __name__=="__main__":
    similarity().call()
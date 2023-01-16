import os
import pandas as pd
import warnings

warnings.filterwarnings(action='ignore')

class spam_stat():
    def __init__(self):
        self.merge()

    def merge(self):
        file_format = "2022" # .csv .xlsx
        file_path = "./spam_data"
        file_list = [f"{file_path}/{file}" for file in os.listdir(file_path) if file_format in file]
        print(file_list)

        merge_df = pd.DataFrame()

        for file_name in file_list:
            file_df = pd.read_excel(file_name, engine="openpyxl", header=1)
            columns = ['신고유형', '스팸유형', '메시지', '메시지 타입']
            temp_df = pd.DataFrame(file_df, columns=columns)
            merge_df = pd.concat([merge_df,temp_df])
        
        # merge_df.to_csv("merge.csv", index=False, encoding='utf-8-sig')


    def split(self):
        total_file = "merge.csv"
        file_df = pd.read_excel(file_name)
        temp_df = pd.DataFrame(file_df, columns=nn)
        twt = Twitter()
        text = ''
        tagging = twt.pos(text)


if __name__=="__main__":
    spam_stat()
import pandas as pd
import os

# 변환할 파일이 들어있는 폴더 경로
folder_path = "C:/Users/junyu/Desktop/JY-Desktop-3070/code/spamdata"
# 폴더 내의 모든 파일 목록 조회
file_list = os.listdir(folder_path)

count = 1
# 모든 xlsx 파일을 csv 파일로 변환
for file_name in file_list:
    # 파일 확장자 확인
    if file_name.endswith(".xlsx"):
        # xlsx 파일을 읽어서 DataFrame으로 변환
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_excel(file_path)
        
        # csv 파일로 저장
        
        csv_file_name = str(count) + ".csv"
        csv_file_path = os.path.join(folder_path, csv_file_name)
        df = df.iloc[:, 8:9]
        df.to_csv(csv_file_path, index=False)
        
        # 변환 완료 메시지 출력
        print(f"{file_name}을 {csv_file_name}로 변환 완료")
        count = count + 1 

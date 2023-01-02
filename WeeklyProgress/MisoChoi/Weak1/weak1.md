#### 요약
- 문자 데이터 수집(백업) 및 전처리
#### 발표 내용
- 수집한 데이터 확인 (사용 가능할지?)
- 스마트폰 문자 백업 및 전처리 방법 안내
----

### 수집한 데이터 확인

- 전처리 완료한 데이터 파일
    
    [sms_preprocessed_miso.csv](https://drive.google.com/file/d/1CzuntZKzFn09iyfXhI281Vdq-53Sg9c7/view?usp=sharing)
    
- 데이터 예시
    
  <img src="https://user-images.githubusercontent.com/78155086/210204997-c966b1d3-1341-404a-b81c-ec348cc861a0.png" width="400">
    
  <img src="https://user-images.githubusercontent.com/78155086/210205183-94dba019-45ab-41a1-8c22-0c9854228465.png" width="400">
    

### 스마트폰 문자 백업 및 전처리 방법 안내

**1. 스마트폰 SMS 메세지 백업 방법 (안드로이드: [[링크]](https://seogilang.tistory.com/1645), 아이폰: ?)**

- SMS Backup & Restore 어플을 다운받고 설명따라서 진행해 주시면 됩니다.
- 저장되는 장소는 설명에 있는 휴대전화  또는 구글 드라이브  등 편하신것으로 선택하시고 백업 파일을 컴퓨터로 옮겨줍니다.

**2. 백업 파일 전처리**

- 백업된 파일은 xml형식이라 이를 csv 형식의 파일로 변환해줘야 합니다.
    - Excel 프로그램을 새로 열고 **‘파일>열기>찾아보기>다운받은 백업파일(xml) 열기’**
    - XML 열기 팝업창이 뜨면 ‘**XML 표로’ 선택 후 확인**
        
      <img src="https://user-images.githubusercontent.com/78155086/210205252-47e0b02b-7b0e-45f5-ac42-1399853fc7df.png" width="200">
        
    - ‘**다른이름으로 저장**’ > 파일 이름 설정, **파일 형식 CSV(쉼표로 분리)**로 지정하여 저장
        
      <img src="https://user-images.githubusercontent.com/78155086/210205334-bbcaaf15-d6ab-4975-ab9d-69fcbb2908f9.png" width="500">
        

- 구글 드라이브에 *sms_backup* 이름의 폴더를 생성하고 csv 형식의 백업 파일을 폴더 내에 둡니다.
- **preprocessing.ipynb [[링크]](https://colab.research.google.com/drive/1WxDLsUEQx9vXiswsuYrALVLh8JVR8VH5?authuser=2#scrollTo=wrJsRKxyeRs_)** 들어가서 ‘**파일>Drive에 사본 저장하기’**
- Colab Notebooks 폴더 내에 위치해 있는 파일을 sms_backup 폴더 내로 이동
- preprocessing.ipynb 안에 백업 파일 불러오는 코드 - 개인 주소와 이름으로 변경
    
    `csv_sms = pd.read_csv('/content/drive/MyDrive/sms_backup/sms_miso.csv')`
    

**[전처리 과정]**

- 필터링1 : 저장된 번호와 주고받은 문자는 제외
- 필터링2 : 개인정보 키워드 입력하여 해당 키워드 포함하는 문자 제외
- 필터링3 : 키워드 익명화 (예: 개인 이름(ex.최미소)을 다른 이름(ex.홍길동)으로 바꾸기)
- 필터링4 : 데이터 다운받은 후 직접 보면서 미처 못지운 개인정보 있으면 지우기

import json
import pandas as pd


def exchange(num, topic_index, filter_str):

    num_json = str(num) +'.json'
    num_csv = "train_" + str(num) +".csv"
    #파일명

    len_num = 6

    with open(num_json, 'r', encoding='UTF-8') as file:
        datas = json.load(file)
        json_test = datas['data']
        #불러옴

        #type_ = []
        topic_ = []
        utterance_ = []
        short_utterance_ = []
        short_topic_ = []
        #초기화

        for k in json_test :
            try:
                t = k['header']['dialogueInfo']
                j = k['body']
                for i in j:
                    for filter_num in filter_str :
                        if filter_num in i['utterance']: 
                            i['utterance'] = str(i['utterance']).replace(filter_num, "") #전처리 -필터링
                    
                    if str(i['utterance']).startswith(' ') :
                        i['utterance'] = str(i['utterance']).replace(' ', "", 1) #전처리 -공백시작제거


                    if( len(i['utterance']) >= len_num ) : #분류 -길이
                        count = 1
                        for n in topic_index :
                            if (n == t['topic']) :
                                topic_.append(str(count))
                            count = count + 1
                        utterance_.append(i['utterance'])

                    else :
                        if((i['utterance'] != '') and (i['utterance'] != ' ') and (i['utterance'] != '  ')) : #공백제거
                            count = 1
                            for n in topic_index :
                                if (n == t['topic']) :
                                    short_topic_.append(str(count))
                                count = count + 1
                            short_utterance_.append(i['utterance'])
                        
            except:
                break
        #추출&누적


        topic2_ = list(set(topic_))
        utterance2_ = list(set(utterance_))
        for ii in range(0,len(utterance2_)-1) :
            topic2_.append(topic2_[0])
        #중복제거
        print("long topic : " + str(len(topic2_)))
        print("long utterance : " + str(len(utterance2_)))

        short_topic2_ = list(set(short_topic_))
        short_utterance2_ = list(set(short_utterance_))

        for ii in range(0,len(short_utterance2_)-1) :
            short_topic2_.append(short_topic2_[0])
        #중복제거2 (합친후 중복제거하면 길이 상관없이 섞여버림)
        print("short topic : " + str(len(short_topic2_)))
        print("short utterance : " + str(len(short_utterance2_)))

        topic2_.extend(short_topic2_)
        utterance2_.extend(short_utterance2_)
        #합침
        print("total topic : " + str(len(topic2_)))
        print("total utterance : " + str(len(utterance2_)))

        df = pd.DataFrame(topic2_, columns = ['topic'])
        df['utterance'] = utterance2_
        #결과저장

        #df.drop_duplicates()
        #df.drop_duplicates(['utterance'], keep='last') 
        #중복제거 안됨

        df.to_csv(num_csv, index = False, encoding="utf-8-sig")
        #csv로 저장

        return len(utterance2_)
    
#---------------------------------------------------------------------------------------------------------------------

def init_run() :
    topic_index = ['개인 및 관계','미용과건강','상거래(쇼핑)','시사교육','식음료','여가생활','일과직업','주거와생활','행사']
    #topic

    filter_str = ['#@이름#','#@시스템','#사진#','#기타#','#@기타#','#@URL#','#@이모티콘#','#검색#','#@소속#', '#@번호#', '#@주소#','Muzi and Friends#','메리_삐짐#'
            ,'(Frodo and Friends#)','Frodo and Friends#', '(Muzi and Friends#)','그레이_삐질#','그레이_부들#','(티엔수분퐁당#)','메리_당황#','메리_헤헷#','밀크_냠냠#'
            ,'뿅유혹1#','메리_냠냠#','뾰옹_꽃#','애교#','멍#','냐옹#','힝#','번쩍#','히죽#','절망#','꾸잉#','#지도#','우웩#','총#','(퓨니#)','하트1#','하트2#','하트3#'
            ,'훌쩍2#','#파일#','흑흑#','눈물#','#송금#','힘듦#','깜짝#', '#동영상#','쑥스#','#삭제#','굿#','열받아#', '훌쩍#', '반함#', '쿨쿨#', '모찌_','케익#'
            ,'감동#','아잉#','축하#','신나#','헉#','뿌듯#','최고#','우와#','졸려#','#@계정#','윙크#','부끄#','하트뿅#','#@전번#','잠#','수줍1#','밥#','배고파#'
            ,'#@금융#','허걱#','입술#','꽃#','#@신원#','오케이#','씨익#','하하#','잘자#','방긋#','뽀뽀#','별#','꺄아#','크크#','흡족#','깜찍#','뻘뻘#','빠직#'
            ,'안도#','하트#','야호#','엉엉#','방긋#','절규#','사랑#','안도#','찔끔#','좋아#','수줍#','뽀뽀1#','심각#','그만#','딸기#','삐짐#','행복#','똥#'
            ,'음표#','멘붕#','궁금#','헤롱#','흥#','와#','부르르#','제발#','근심#','미소#','뽀뽀2#','버럭#','악마#','곤란#','짜증#','담배#','소주#','찡긋#'
            ,'메롱#','으헤헤#','정색#','잘난척#','브이#','삐질#','화남#','분노#','당황#','민망#','기대#','썩소#','발그레#','공포#','맥주#','~#','#~']
    #필터

    data_num = 0

    for zzz in range(1,10):
        print("----------------------------------------")
        print("페이즈 : " + str(zzz))
        print("----------------------------------------")
        data_num = data_num + exchange(zzz,topic_index,filter_str)
    print("----------------------------------------")
    #반복호출
    print()
    print("========================================")
    print("data_num = " + str(data_num))
    print("========================================")
    print()

#---------------------------------------------------------------------------------------------------------------------
init_run()



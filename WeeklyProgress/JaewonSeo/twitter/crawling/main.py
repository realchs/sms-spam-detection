import twitter
import key
import pandas as pd
from time import sleep

twitter_consumer_key = key.arr.API_Key
twitter_consumer_secret = key.arr.API_Key_Secret
twitter_access_token = key.arr.Access_Token
twitter_access_secret = key.arr.Access_Token_Secret
twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                    consumer_secret=twitter_consumer_secret,
                    access_token_key=twitter_access_token, 
                    access_token_secret=twitter_access_secret)

def keyword(query, output_file_name):
        statuses = twitter_api.GetSearch(term=query, count=100000000)

        # for status in statuses:
        #     print(status.text)

        with open(output_file_name, "a", encoding="utf-8") as output_file:
            for status in statuses:
                print(status.text, file=output_file)

if __name__=="__main__":
    arr1 = pd.read_excel("word.xls", usecols=["단어"])
    print(arr1)
    df_dic = arr1.to_dict()
    arr2 = df_dic["단어"].values()
    arr2_list = list(arr2)
    print(arr2_list)
    arrs = ["진짜", "", "했어"]
    for arr in arr2_list:
        keyword(arr, "talk.txt")
        sleep(10)
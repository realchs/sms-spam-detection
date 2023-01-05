import twitter
import key


twitter_consumer_key = key.arr.API_Key
twitter_consumer_secret = key.arr.API_Key_Secret
twitter_access_token = key.arr.Access_Token
twitter_access_secret = key.arr.Access_Token_Secret
twitter_api = twitter.Api(consumer_key=twitter_consumer_key,
                    consumer_secret=twitter_consumer_secret,
                    access_token_key=twitter_access_token, 
                    access_token_secret=twitter_access_secret)

def keyword(query, output_file_name):
        statuses = twitter_api.GetSearch(term=query, count=1000)

        for status in statuses:
            print(status.text)

        with open(output_file_name, "a", encoding="utf-8") as output_file:
            for status in statuses:
                print(status.text, file=output_file)

if __name__=="__main__":
    arrs = ["근데", "그냥", "했어"]
    for arr in arrs:
        keyword(arr, "대화.txt")
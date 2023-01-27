# Chat-GPT API

### 사용법

1. git clone [https://github.com/transitive-bullshit/chatgpt-api.git](https://github.com/transitive-bullshit/chatgpt-api.git)
2. `npm install chatgpt puppeteer`
3. .env 파일 생성
    
    ```bash
    # ------------------------------------------------------------------------------
    # This is an example .env file.
    #
    # All of these environment vars must be defined either in your environment or in
    # a local .env file in order to run the demo for this project.
    # ------------------------------------------------------------------------------
    
    # -----------------------------------------------------------------------------
    # ChatGPT
    # -----------------------------------------------------------------------------
    
    OPENAI_EMAIL=EMAIL_작성
    OPENAI_PASSWORD=PASSWORD_작성
    ```
    
4. ‘./demos/txt-conversation.ts 생성
    
    ```bash
    import dotenv from 'dotenv-safe'
    import { oraPromise } from 'ora'
    
    import { ChatGPTAPIBrowser } from '../src'
    
    import * as fs from 'fs'
    dotenv.config()
    
    async function main() {
      const email = process.env.OPENAI_EMAIL
      const password = process.env.OPENAI_PASSWORD
    
      const api = new ChatGPTAPIBrowser({
        email,
        password,
        debug: false,
        minimize: true
      })
      await api.initSession()
    
      var prompts = fs.readFileSync('./data/prompts.txt').toString().split("\n");
      var answers = fs.createWriteStream('./data/answers.txt');
      answers.on('error', function(err) { /* error handling */ });
      
    
      let res = await oraPromise(api.sendMessage(prompts['0']), {
        text: prompts['0']
      })
        console.log(prompts['0']);
        console.log('\n' + res.response + '\n')
        answers.write('\n---------------------------------------------------');
        answers.write('\nANSWER\n');
        answers.write(res.response);
    
      for(var i in prompts) {
    
        if(i!='0'){
          res = await oraPromise(
            api.sendMessage(prompts[i], {
              conversationId: res.conversationId,
              parentMessageId: res.messageId
            }),
            {
              text: prompts[i]
            }
          )
          console.log(prompts[i]);
          console.log('\n' + res.response + '\n')
          answers.write('\n---------------------------------------------------');
          answers.write('\nANSWER\n');
          answers.write(res.response);
        }
      }
      // close the browser at the end
      answers.end();
      await api.closeSession()
    }
    
    main().catch((err) => {
      console.error(err)
      process.exit(1)
    })
    ```
    
5. ‘./data/prompts.txt’ 생성
    
    **예시**
    
    ```bash
    Write a poem about cats.
    Can you make it cuter and shorter?
    Now write it in Korean.
    What were we talking about again?
    ```
    
    - 지금은 \n로 질문 구분하게 해둠. 필요시 변경
6. 실행

```bash
npx tsx demos/txt-conversation.ts
```

1. 결과

    <img src="https://user-images.githubusercontent.com/78612464/215012389-8a8340f6-f948-4612-ba1b-f163e302a411.png"  width="600">
    
    - 데이터 처리를 위해서 대답 구분자 변경 필요

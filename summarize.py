import os
import openai
import time
import tiktoken

def summarize(api_key, text_file):
    openai.api_key = api_key
    with open(text_file, "r") as f:
        transcript = f.read()

    # Cut the transcript to meet the token limit (4096 in gpt-3.5-turbo)
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    token_count = len(encoding.encode(text))
    division_number = token_count // 4096 + 2
    length = len(transcript)
    transcript = [transcript[i * length // division_number: (i + 1) * length // division_number] for i in range(division_number)]

    # transcript summarization by chatgpt
    for trans in transcript: 
        content = "以下我會提供一個課程錄音稿，請幫我以英文條列式地總結錄音稿的內容，整理形式請依照(1)(a)(b)...(2)...：" + trans
        messages = [{"role": "user", "content": content}]
        
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        )

        chat_response = completion
        answer = chat_response.choices[0].message.content
        print(f'ChatGPT: {answer}')

        # Overwhemled requests crashes the server
        time.sleep(10)
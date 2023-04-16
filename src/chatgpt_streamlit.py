import streamlit as st
import os
import openai

#openai.api_key = "xxxxxxxx"
openai.api_key = os.environ["OPENAI_API_KEY"]

st.title("ChatGPT API")
query_text = st.text_input("どんなことに悩んでいますか")
bot_character = st.selectbox("誰に相談したいですか" , ["紳士", "子育て中の30代のママ", "子育てを終えた55歳の女性", "鬼軍曹", "2000年代のギャル"])
advise_level = st.selectbox("どれくらい聞きたいですか" , ["簡単に", "詳しく"])

def chatgpt_Q(query, chara="紳士", level="簡単に"):
  res = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      messages = [
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "{}のような口調で教えてください。依頼者が「{}」という悩みを持っています。気持ちに寄り添った姿勢を見せながら、{}アドバイスをしていただけますか。".format(chara, query,level)}
      ]
  )
  res_content = res["choices"][0]["message"]["content"]
  return res_content

execute = st.button("相談する")
if execute:
    if query_text:
        answer = chatgpt_Q(query_text, chara=bot_character, level=advise_level)
        st.write(answer)
    else:
        st.write("悩み事を入力してください")



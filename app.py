import streamlit as st
import random

st.title("🦄 ユニコーンとあそぼ ✨")

st.write("ユニコーンに名前をつけてね！")

unicorn_name = st.text_input("ユニコーンの名前", "キララ")

st.write(f"### 🦄 {unicorn_name}ちゃん")

action = st.selectbox(
    "何してあそぶ？",
    ["おはなしする 💭", "ジャンプする 🌟", "にじを作る 🌈", "まほうをかける ✨"]
)

if st.button("あそぶ！"):
    if "おはなし" in action:
        messages = [
            f"{unicorn_name}: キラキラの森であそぼう！✨",
            f"{unicorn_name}: 今日はとってもいい天気だね！☀️",
            f"{unicorn_name}: あなたと友だちになれてうれしい！💕",
            f"{unicorn_name}: いっしょにぼうけんにいこう！🌟"
        ]
        st.success(random.choice(messages))
    elif "ジャンプ" in action:
        st.info(f"🦄 {unicorn_name}が高くジャンプしたよ！ぴょーん！")
        st.balloons()
    elif "にじ" in action:
        st.success(f"🌈 {unicorn_name}がキレイなにじを作ったよ！")
        st.write("💗💛💚💙💜")
    else:
        st.warning(f"✨ {unicorn_name}がまほうをかけたよ！キラキラ〜✨")
        st.snow()

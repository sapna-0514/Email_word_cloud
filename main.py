
import streamlit as st
import mailbox
from collections import Counter
import string
from wordcloud import WordCloud
import matplotlib.pyplot as plt

uploaded_file = st.file_uploader("Upload an .mbox file", type="mbox")

if uploaded_file is not None:
    mbox = mailbox.mbox(uploaded_file.name)
    all_words = []

    for message in mbox:
        body = message.get_payload()
        if body:
            body = body.lower()
            body = body.translate(str.maketrans('', '', string.punctuation))
            words = body.split()
            all_words.extend(words)

    count = Counter(all_words)
    st.write("Top 10 words:", count.most_common(10))

    wc = WordCloud(width=800, height=400, background_color='white')
    wc.generate_from_frequencies(count)

    st.image(wc.to_array(), use_column_width=True)

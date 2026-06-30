
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.title("Email Word Cloud Generator")

uploaded_file = st.file_uploader("Upload your email text file", type=["txt"])

if uploaded_file is not None:
    # Read file content
    text = uploaded_file.read().decode("utf-8")

    # Show raw text
    st.subheader("Email Content")
    st.text(text)

    
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    
    st.subheader("Word Cloud")
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

    
    st.download_button(
        label="Download Word Cloud Text",
        data=text,
        file_name="email_output.txt",
        mime="text/plain"
    )


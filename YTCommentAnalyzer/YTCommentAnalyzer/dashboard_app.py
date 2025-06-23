import streamlit as st
from sentiment_analyzer import process_video_comments
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.title("🎥 YouTube Comment Sentiment Analyzer")

video_url = st.text_input("Enter YouTube Video URL:")

def extract_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1]
    return None

if st.button("Analyze"):
    video_id = extract_video_id(video_url)
    if video_id:
        with st.spinner("Fetching and analyzing comments..."):
            df = process_video_comments(video_id)

        st.success("Analysis Complete!")
        st.write(df.head())

        st.subheader("📊 Sentiment Distribution")
        sentiment_counts = df['Sentiment'].value_counts()
        st.bar_chart(sentiment_counts)

        st.subheader("☁️ Word Cloud of Comments")
        text = " ".join(df['Comment'].tolist())
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        st.pyplot(plt)
    else:
        st.error("Invalid YouTube URL!")

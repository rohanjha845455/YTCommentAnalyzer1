# 🎥 YouTube Comment Sentiment Analyzer

This Python project fetches YouTube video comments, performs sentiment analysis using TextBlob, and visualizes the results with charts and word clouds.

## 📦 Features
- Fetches top comments via YouTube Data API
- Analyzes sentiment: Positive / Negative / Neutral
- Streamlit dashboard with charts & word cloud

## 🚀 How to Run

1. Clone this repo
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Add your YouTube API key in `api_key.json`
4. Run:
    ```
    streamlit run dashboard_app.py
    ```

## 🛠️ Tech Stack
- Python
- YouTube Data API
- TextBlob
- Pandas
- Streamlit
- WordCloud

## 📌 Example Input
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

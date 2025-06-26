from googleapiclient.discovery import build
from textblob import TextBlob
import pandas as pd
import json

import streamlit as st

def load_api_key():
    with open('api_key.json') as f:
        return json.load(f)['api_key']

def get_youtube_service():
    api_key = load_api_key()
    return build('youtube', 'v3', developerKey=api_key)

def fetch_comments(video_id, max_results=100):
    service = get_youtube_service()
    comments = []

    response = service.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
        textFormat="plainText"
    ).execute()

    while response and len(comments) < max_results:
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)
        if 'nextPageToken' in response:
            response = service.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=100,
                pageToken=response['nextPageToken'],
                textFormat="plainText"
            ).execute()
        else:
            break

    return pd.DataFrame(comments[:max_results], columns=['Comment'])

def analyze_sentiment(comment):
    polarity = TextBlob(comment).sentiment.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

def process_video_comments(video_id):
    df = fetch_comments(video_id)
    df['Sentiment'] = df['Comment'].apply(analyze_sentiment)
    return df

import streamlit as st
from sumapi.api import SumAPI

api = SumAPI(username='kave', password='kave')

def get_sentiment(text: str):
    result = api.sentiment_analysis(text, domain='general')
    print(result)
    try:
        cevap = result['evaluation']['label']
    except:
        cevap = result
    return cevap

def get_color(sentiment):
    # Duygu analizine göre renk döndür
    if sentiment == "Pozitif":
        return "#A8E6CF"  # Pastel Yeşil
    elif sentiment == "Negatif":
        return "#FF8A80"  # Pastel Kırmızı
    elif sentiment == "Nötr":
        return "#FFD3B6"  # Pastel Turuncu
    else:
        return "#FFFF00" # Sarı

st.title("SumAPI Duygu Analizi Uygulaması")

user_input = st.text_input("Bir şeyler yazın:")

if user_input:
    sentiment = get_sentiment(user_input)
    color = get_color(sentiment)
    st.write(f'<div style="color: {color};">Duygu Analizi Sonucu: {sentiment}</div>', unsafe_allow_html=True)

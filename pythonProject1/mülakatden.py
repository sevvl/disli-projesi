import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import requests
from bs4 import BeautifulSoup

# 05/05/2024
module_url = "https://tfhub.dev/google/universal-sentence-encoder/1?tf-hub-format=compressed"
embed = hub.load(module_url)

# Veritabanı simülasyonu
database = {}

def analyze_text(text):
    # Metni analiz kısmına çok hakim olmadığım için basitleştirmek istedim.senero 1 e göre bir basitleştirme yapıldı.
    topics = {
        "kitap": ["edebiyat", "roman", "bilim kurgu"],
        "bilim": ["fizik", "kimya", "biyoloji"],
        "biyoloji": ["hücre", "genetik", "evrim"]
    }
    general_topics = {key: value for key, value in topics.items() if any(word in text for word in key.split())}
    return general_topics

def internetten_arama_yap(topics):
    # İnternet üzerinden bilgi arama ve başlık alma
    results = {}
    for topic, subtopics in topics.items():
        for sub in subtopics:
            url = f"https://tr.wikipedia.org/wiki/{sub}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.find("h1", {"id": "firstHeading"}).text
            results[sub] = title
    return results

def save_to_database(topic_info, search_results):
    # Veritabanına bilgi kaydetme
    database.update({**topic_info, **search_results})
    print("Veri tabanına kaydedildi: ", database)

def main():
    user_inputs = []
    while True:
        text = input("Lütfen bir metin girin (çıkmak için 'exit' yazın): ")
        if text.lower() == "exit":#bu kodda garantiye almak için küçük harfe dönüştürüldü 30/04/2024
            break
        user_inputs.append(text)#bu kodda girilen text user_inputsa atılıyor30/04/2024

    # Ortak konuları bulma ve analiz etme
    all_topics = [analyze_text(text) for text in user_inputs]
    common_topics = set.intersection(*map(set, all_topics))

    if common_topics:
        print("Ortak konular:", common_topics)
        for topic in common_topics:
            sub_topics = list(set([sub for t in all_topics for sub in t.get(topic, [])]))
            search_results = search_internet({topic: sub_topics})
            save_to_database({topic: sub_topics}, search_results)

if _name_ == "_main_":
    main()
# not: ben daha çok görüntü işleme konuları ile ilgilendiğim için bu task de biraz zorlandım. yapabildiğim kadar yapmaya
# çalıştım. bana eksik olduğum konular üzerindeki tavsiyelerinizi dinlemekten mutlu olurum.teşekkür ederim.
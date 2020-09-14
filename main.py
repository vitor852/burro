import speech_recognition as sr
import spacy
import pandas
import sys

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

nlp = spacy.load("pt_core_news_sm")
vectorizer = TfidfVectorizer()
cat_vectorizer = CountVectorizer()
model = MultinomialNB()

def listen() -> str:
    microphone = sr.Recognizer()

    with sr.Microphone() as source:
        microphone.adjust_for_ambient_noise(source)

        print(":")

        audio = microphone.listen(source)

        try:
            sentence = microphone.recognize_google(audio, language="pt-BR")
            print(sentence)

            return sentence.lower()

        except:
            print("erro")


def pre_processing_data(data: str) -> str:
    tokenized_sentence = nlp(data)
    filtered_sentence = ""

    for i in tokenized_sentence:
        if(not i.is_stop):
            filtered_sentence += " " + i.lemma_

    return filtered_sentence.strip()

def read_data() -> list:
    path_name = sys.argv[1]

    data = pandas.read_csv(path_name)
    categories = data["categories"]

    processed_data = []

    for sentence in data["sentence"]:
        processed_sentece = pre_processing_data(sentence)

        processed_data.append(processed_sentece)

    return processed_data, categories

data, categories = read_data()
categories_dictionary = {}

for number, element in enumerate(set(categories)):
    categories_dictionary[element] = number

Y = [categories_dictionary[cat] for cat in categories]
X = vectorizer.fit_transform(data)

model.fit(X, Y)

while True:
    sentence = listen()
    sentence = pre_processing_data(sentence)
    sentence = vectorizer.transform([sentence])

    result = model.predict(sentence)

    for i in categories_dictionary.items():
        if(i[1] == result):
            print(i[0])
    
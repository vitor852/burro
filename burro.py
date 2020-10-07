from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import speech_recognition as sr
import spacy
import pandas

DATA_PAHT = './data/train.csv'

vectorizer = TfidfVectorizer()
cat_vectorizer = CountVectorizer()
model = MultinomialNB()

nlp = spacy.load("pt_core_news_sm")


class Burro:
    def __init__(self):
        microphone = sr.Microphone()
        recognizer = sr.Recognizer()

        recognizer.energy_threshold = 200

        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)

        stop_listening = recognizer.snowboy_wait_for_hot_word('')

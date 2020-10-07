import sys
from playsound import playsound

def pre_processing_data(data: str) -> str:
    """
        Clear user phrase.

        Implemets all seteps of pre processing data.
        The sentence pass thro tokenization and lemmatization.

        Parameters
        __________
        data
            the user sentence
    """

    tokenized_sentence = nlp(data)
    filtered_sentence = ""

    for i in tokenized_sentence:
        if(not i.is_stop):
            filtered_sentence += " " + i.lemma_

    return filtered_sentence.strip()

def read_data() -> list:
    """
        read the data so that the implementation of the algorithm is possible

    """

    data = pandas.read_csv(DATA_PATH)
    categories = data["categories"]

    processed_data = []

    for sentence in data["sentence"]:
        processed_sentece = pre_processing_data(sentence)

        processed_data.append(processed_sentece)

    return processed_data, categories

def choose(category: int, sentence: str):
    """
        Execute the predicted category.
    """

    if(category == "time"):
        import datetime

        now = datetime.datetime.now()

        print(now)

    elif(category == "playMusic"):
        from youtube_search import YoutubeSearch
        import webbrowser

        sentence = sentence.replace("tocar", "")

        default = "https://www.youtube.com"

        results = YoutubeSearch(sentence[2:], max_results=1).to_dict()

        print(sentence[2:])

        webbrowser.open(default + results[0]["url_suffix"], autoraise=True)
        

data, categories = read_data()
categories_dictionary = {}

for number, element in enumerate(set(categories)):
    categories_dictionary[element] = number

Y = [categories_dictionary[cat] for cat in categories]
X = vectorizer.fit_transform(data)

model.fit(X, Y)

def verify_call(sentence: str) -> bool:
    """
        Checks if the hot word is the first word in sentence
    """

    sentence = sentence.split()
    if(sentence[0] == "burro"):
        return True
    else:
        return False

def handle_sentence(recognizer, audio):
    """
        Apply the recognition algorithms and remove the hot word.
    """

    try:
        sentence = recognizer.recognize_google(audio, language="pt-BR")
        has_call = verify_call(sentence)

        if(has_call):
            sentence = sentence.replace("burro", "")

            # processed_sentence = pre_processing_data(sentence)
            vectorized_sentence = vectorizer.transform([sentence])

            result = model.predict(vectorized_sentence)

            for i in categories_dictionary.items():
                if(i[1] == result):
                    choose(i[0], sentence)

    except sr.UnknownValueError:
        print("Não entendi")
    except sr.RequestError:
        print("Falha internet")

while(True):
    continue
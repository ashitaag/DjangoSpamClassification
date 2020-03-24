import json
import requests


def calculateProbability(word, word_dict, b_c):
    ans = (word_dict + 1)/(b_c)
    return ans**(1./10)

def predict(email):

    data = requests.get('http://localhost:8000/static/data1.json').json()
    email_new = email.replace('\n', ' ').split()
    P1 = 0.5
    P2 = 0.5
    for word in email_new:
        if word in data['spamwords']:
            P1 *= calculateProbability(word, data['spamwords'][word], data['no_unique_words']+ data['spam_count'])
        if word in data['hamwords']:
            P2 *= calculateProbability(word, data['hamwords'][word], data['no_unique_words']+ data['ham_count'])
    print("P1 is", P1)
    print("P2 is", P2)
    if P1 > P2:
        return "spam"
    else:
        return "ham"

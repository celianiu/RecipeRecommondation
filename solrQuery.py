from urllib.request import urlopen
import json
import parseInput
import urllib.parse
import math
import re
from collections import Counter
#from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
#from sklearn.metrics.pairwise import cosine_similarity
import random


def indexing(input):
    # ings = parseInput.ingredient_parser("beef, lemons")
    ings = parseInput.ingredient_parser(input)
    q = "preProcessedIngredient:" + "(" + ",".join(ings) + ")"
    print(q)
    solr_tuples = [
        # text in search box
        ('q', q),
        # how many products do I want to return
        ('q.op', "AND"),
        ('wt', 'json')
    ]
    solr_url = 'http://localhost:8983/solr/copy/select?'
    encoded_solr_tuples = urllib.parse.urlencode(solr_tuples)
    complete_url = solr_url + encoded_solr_tuples
    connection = urlopen(complete_url)
    response = json.load(connection)
    print(response['response']['numFound'], "documents found.")
    # print(response['response']['docs'][0])
    return response['response']['docs']

    # Print the name of each document.
    # count = 0
    # for document in response['response']['docs']:
    #   print("Name =", document['food_title'])
    #   count+=1
    #   if count==10:
    #     break;


#

# def randomSearchResult(documents):
#     titles = []
#     docs = []
#     for d in documents:
#         if len(docs) != 0 and d['food_title'][0] == docs[len(docs) - 1]['food_title'][0]:
#             continue
#
#         titles.append(d['food_title'][0])
#         docs.append(d)
#         if len(docs) == 10:
#             break
#
#     # print(docs)
#     return titles, docs

def cosineSimilarity(input, documents):
    ings = parseInput.ingredient_parser(input)
    titles = []
    docs=[]
    Cosine = {}

    for d in documents:
        if len(docs) != 0 and d['food_title'][0] == docs[len(docs) - 1]['food_title'][0]:
            continue

        vector1 = text_to_vector(d['preProcessedIngredient'])
        # d['preProcessedIngredient']
        vector2 = text_to_vector(ings)
        cosine = get_cosine(vector1, vector2)
        Cosine[d['food_title'][0]] = cosine

    Cos = sorted(Cosine.items(), key=lambda x: x[1])
        # Cosine.sorted(key = lambda x:x[1])
    print(Cos)
    for key in range(len(Cos)):
        titles.append(Cos[key][0])
        if len(titles) == 10:
            break
    # return titles
    return titles

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    #WORD = re.compile(r"\w+")
    #words = WORD.findall(text)
    #print(words)
    return Counter(text)

def searchByRecipeName(name):
    q = "food_title:" + name
    solr_tuples = [
        # text in search box
        ('q', q),
        # how many products do I want to return
        ('q.op', "or"),
        ('wt', 'json')
    ]
    solr_url = 'http://localhost:8983/solr/copy/select?'
    encoded_solr_tuples = urllib.parse.urlencode(solr_tuples)
    complete_url = solr_url + encoded_solr_tuples
    connection = urlopen(complete_url)
    response = json.load(connection)
    # print(name)
    # print(response['response']['docs'])
    return response['response']['docs'][0]

# documents = indexing("beef, lemons")
# randomSearchResult(documents)

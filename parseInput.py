import nltk
import string
import ssl
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

#from sklearn.metrics.pairwise import cosine_similarity
import math
#
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('omw-1.4')


measurement = [
        "teaspoon",
        "t",
        "tsp.",
        "tablespoon",
        "T",
        "tbl.",
        "tb",
        "tbsp.",
        "fluid ounce",
        "fl oz",
        "gill",
        "cup",
        "c",
        "pint",
        "p",
        "pt",
        "fl pt",
        "quart",
        "q",
        "qt",
        "fl qt",
        "gallon",
        "g",
        "gal",
        "ml",
        "milliliter",
        "millilitre",
        "cc",
        "mL",
        "l",
        "liter",
        "litre",
        "L",
        "dl",
        "deciliter",
        "decilitre",
        "dL",
        "bulb",
        "level",
        "heaped",
        "rounded",
        "whole",
        "pinch",
        "medium",
        "slice",
        "pound",
        "lb",
        "#",
        "ounce",
        "ounc",
        "oz",
        "mg",
        "milligram",
        "milligramme",
        "g",
        "gram",
        "gramme",
        "kg",
        "kilogram",
        "kilogramme",
        "x",
        "of",
        "mm",
        "millimetre",
        "millimeter",
        "cm",
        "centimeter",
        "centimetre",
        "m",
        "meter",
        "metre",
        "inch",
        "in",
        "milli",
        "centi",
        "deci",
        "hecto",
        "kilo",
    ]

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
def remove_punc(query):
    query = [i for i in nltk.word_tokenize(query) if i not in string.punctuation]
    #print(query)
    return query

def remove_stopWord(qlist):
    stopWords = set(stopwords.words('english'))
    new_query = []
    for w in qlist:
        if w not in stopWords:
            new_query.append(w)
    #print(new_query)
    return new_query

def caseFolding(qlist):
    new_query = []
    for w in qlist:
        new_query.append(w.casefold())
    #print(new_query)
    return new_query

def stemming(qlist):

    new_query = []
    for w in qlist:
        new_query.append(stemmer.stem(w))
    #print(new_query)
    return new_query

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None # for easy if-statement

def lemmatization(qlist):

    tagged = nltk.pos_tag(qlist)
    new_query = []
    for w, tag in tagged:
        wntag = get_wordnet_pos(tag)
        if wntag == None:
            new_query.append(lemmatizer.lemmatize(w))
        else:
            new_query.append(lemmatizer.lemmatize(w,pos=wntag))
    #print(new_query)
    return new_query


def ingredient_parser(inputs):
    #TODO: remove non alphabet letter
    #TODO: remove measurment

    tokens = remove_punc(inputs)
    #print("-----------case-folding-----------")
    tokens = caseFolding(tokens)
    #print("-----------lemmatization-----------")
    tokens = lemmatization(tokens)
    #print("-----------Stemming-----------")
    tokens = stemming(tokens)
    #print("-----------remove stop words-----------")
    tokens = remove_stopWord(tokens)
    tokens = [word for word in tokens if word.isalpha()]
    tokens = [word for word in tokens if word not in measurement]
    return tokens

ingredient_parser("beef, lemons, cucumber")

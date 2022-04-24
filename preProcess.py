import os
from urllib.request import urlopen
import json
import parseInput
import urllib.parse
from os import listdir
from os.path import isfile, join

folder = "/Users/yuxinkang/Desktop/Rice/631/ScrapedData"
count = 0
for file in os.listdir(folder):
    #print(file)
    count+=1;
    with open(os.path.join(folder,file), 'rb') as f:
        flag = True
        try:
            data = json.load(f)
            ingredients = data['food_ingredient']
            newIngs = []
            for ing in ingredients:
                newIngs+= parseInput.ingredient_parser(ing)
            data['preProcessedIngredient'] = newIngs # <--- add `id` value.
        except:
            flag = False
            print("error line{0}".format(count))
    with open(os.path.join(folder,file), "w") as f:
        if (flag):
            json.dump(data, f)


    if (count%1000==0):
        print(count)
# solr_tuples = [
#     # text in search box
#     ('q', "*:*"),
#     # how many products do I want to return
#     ('q.op', "AND"),
#     ('wt', 'json'),
#     ('fl', 'recipes_id, food_ingredient'),
# ]
# solr_url = 'http://localhost:8983/solr/my_core/select?'
# encoded_solr_tuples = urllib.parse.urlencode(solr_tuples)
# complete_url = solr_url + encoded_solr_tuples
# connection = urlopen(complete_url)
# response = json.load(connection)
# print(response['response']['numFound'], "documents found.")
# documents = response['response']['docs']
# ids = []
# ingredients = []
# for d in documents:
#     ids.append(d['recipes_id'][0])
#     ingredients.append(d['food_ingredient'])
#
#
# print(ids[0:10])


# solrConect = SolrClient("http://localhost:8983/solr/my_core/solr/update?")
# doc = [{'id': 'my_id', 'count_related_like':{'set': 10}}]
# solrConect.index_json("my_collection", json.dumps(doc) )
# solrConect.commit("my_collection", softCommit=True)
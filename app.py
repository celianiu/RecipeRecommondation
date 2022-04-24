from flask import Flask,send_from_directory,request,jsonify
import solrQuery
from flask_cors import CORS, cross_origin
from urllib.parse import unquote
#solr returned all recipes
documents=[]
# randomed 10 recipe
docs = []
app = Flask(__name__,static_url_path='', static_folder='recipe/public')
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def mainPage():
    return 'hello world'

@app.route('/search/<searchQuery>', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def search(searchQuery):
    titles = []
    if request.method == 'POST':
        global documents,docs
        documents = solrQuery.indexing(searchQuery)
        #titles,docs= solrQuery.randomSearchResult(documents)
        titles = solrQuery.cosineSimilarity(searchQuery,documents)
    #return 'hello world'
    #print(docs)
    return jsonify(titles)

@app.route('/recom/<recipName>', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def recommend(recipName):
    # res={}
    # if request.method == 'POST':
    #     for d in docs:
    #         if d['food_title'][0]== unquote(recipName):
    #             res = d
    #             break
    # print(res)
    res = solrQuery.searchByRecipeName(unquote(recipName))

    if ('nutrients.calories' in res.keys()):
        return {
        "food_title": res["food_title"][0],
        "link":res['link'][0],
        "ingredient":' \n\n '.join(res['food_ingredient'][:]),
        "instruction": ' \n\n '.join(res['instruction'][:]),
        "nutrients":
            "Calories: {0}"
            "\nFat: {1}"
            "\nSaturatedFat: {2}"
            "\nCholesterol: {3}"
            "\nSodium: {4}"
            "\nCarbohydrate: {5}"
            "\nFiber: {6}"
            "\nSugar': {7}"
            "\nProtein: {8}".format(res['nutrients.calories'][0],
                                    res['nutrients.fatContent'][0],
                                    res['nutrients.saturatedFatContent'][0],
                                    res['nutrients.cholesterolContent'][0],
                                    res['nutrients.sodiumContent'][0],
                                    res['nutrients.carbohydrateContent'][0],
                                    res['nutrients.fiberContent'][0],
                                    res['nutrients.sugarContent'][0],
                                    res['nutrients.proteinContent'][0])

        }
    else:
        return{
            "food_title": res["food_title"][0],
            "link": res['link'][0],
            "ingredient": ' \n\n '.join(res['food_ingredient'][:]),
            "instruction": ' \n\n '.join(res['instruction'][:]),
            "nutrients":None
        }



    #return 'hello world'

@app.route('/refresh', methods=['POST', 'GET'])
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def refresh():
    global docs
    if request.method == 'GET':
        titles, docs = solrQuery.randomSearchResult(documents)
    return jsonify(titles)



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)
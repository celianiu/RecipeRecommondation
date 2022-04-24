import random
from recipe_scrapers import scrape_me
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# DRIVER_PATH = 'C:/Users\Yuhua\Documents\webdriver\chromedriver.exe'
# driver = webdriver.Chrome(executable_path = DRIVER_PATH)

count = 0

for id in range(1001,111111):

    url = 'https://www.food.com/recipe/{0}'.format(id)
    #url = 'https://www.allrecipes.com/recipe/6663'
    try:
        #url = 'https://www.allrecipes.com/recipe/342043/'
        #driver.get(url)
        scraper = scrape_me(url, wild_mode=True)
        title = scraper.title()
        title = title.replace('/', '_')
        title = title.replace('"','_')
        title = title.replace(',','_')
        if title == 'Whoops...':
            print(id)
            continue

    except:
        print(id)
        continue
    # try:
    #     close_popup = driver.find_element(By.CLASS_NAME, 'bx-close-x-adaptive-1')
    #     close_popup.click()
    # except:
    #     close_popup = "None"


    try:
        total_time = scraper.total_time()
    except:
        total_time = None

    try:
        yields = scraper.yields()
    except:
        yields = None

    try:
        ingredient = scraper.ingredients()
    except:
        ingredient = None

    try:
        instruction = scraper.instructions()
    except:
        instruction = None

    try:
        rating = scraper.ratings()
    except:
        rating = None

    try:
        nutrients = scraper.nutrients()
    except:
        nutrients = None
    # open chormw windows with given url



    # commands = []
    reviews = []
    # try:
    #     commend_section = driver.find_element(By.CLASS_NAME, 'feedback__bodyContainer')
    #     commands = commend_section.find_elements(By.CLASS_NAME, 'feedback__reviewBody')
    #     for c in commands:
    #         body = c.text
    #         reviews.append(body)
    #
    # except:
    #     reviews = []



    foodData = {
        "recipes_id": id,
        "food_title": title,
        "rating": rating,
        "total_time:": total_time,
        "yield:": yields,
        "food_ingredient": ingredient,
        "instruction": instruction,
        "link": url,
        "nutrients": nutrients,
        "reviews": reviews
    }

    # food_object = json.dumps(foodData, indent=4)
    # with open("/Users/yuxinkang/Desktop/Rice/631/ScrapedData/(food){0}_{1}.json".format(title, id),
    #           "w") as outfile:
    #     outfile.write(food_object)

    food_object = json.dumps(foodData, indent=4)
    with open("C:/Users/Yuhua/Desktop/grad school/631/ScrapedData/(food){0}_{1}.json".format(title, id),
              "w") as outfile:
        outfile.write(food_object)

    # if count == 100:
    #     driver.implicitly_wait(10)
    # else:
    #     driver.implicitly_wait(1)
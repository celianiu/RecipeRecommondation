import random

from recipe_scrapers import scrape_me
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

DRIVER_PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(executable_path = DRIVER_PATH)

with open('links.json') as f:
    count = 0
    for url in f:
        count+=1
        #url = 'https://www.foodnetwork.com/recipes/ina-garten/16-bean-pasta-e-fagioli-3612570'
        url = url.replace('\n','')
        scraper = scrape_me(url, wild_mode=True)
        id = url.split('-')[-1]
        #
        # # Q: What if the recipe site I want to extract information from is not listed below?
        # # A: You can give it a try with the wild_mode option! If there is Schema/Recipe available it will work just fine.
        #
        # print(
        try:
            title = scraper.title()
            title = title.replace('/','_')
        except:
            print(count)
            continue
        try:
            total_time = scraper.total_time()
        except:
            total_time = None

        yields = scraper.yields(),
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
            instruction= None

        try:
            links = scraper.links()
        except:
            links = None

        try:
            nutrients = scraper.nutrients()
        except:
            nutrients = None
        #open chormw windows with given url
        driver.get(url)
        commands = []
        reviews = []
        try:
            commend_section = driver.find_element(By.XPATH, '//*[@id="mod-user/comments-feed-1"]/div[3]')
            commands = commend_section.find_elements(By.CLASS_NAME, 'comment ')

            for c in commands:
                try:
                    body = c.find_element(By.CLASS_NAME, 'comment-body').text
                except:
                    continue
                reviews.append(body)
        except:
            reviews = []


        foodData = {
            "recipes_id": id,
            "food_title": title,
            "total_time:": total_time,
            "yield:": yields,
            "food_ingredient": ingredient,
            "instruction": instruction,
            "link": url,
            "nutrients": nutrients,
            "reviews":reviews
        }

        food_object = json.dumps(foodData, indent=4)
        with open("/Users/yuxinkang/Desktop/Rice/631/ScrapedData/{0}_{1}.json".format(title,id),
                  "w") as outfile:
            outfile.write(food_object)
        if count == 100:
            driver.implicitly_wait(20)
        else:
            driver.implicitly_wait(random.random())


    #print(url) # 每行末尾会有一个换行符


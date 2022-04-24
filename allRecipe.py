import random
from recipe_scrapers import scrape_me
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

DRIVER_PATH = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(executable_path = DRIVER_PATH)

count = 0

for id in range(15275,120000):
    count+=1
    url = 'https://www.allrecipes.com/recipe/{0}'.format(id)
    #url = 'https://www.allrecipes.com/recipe/6663'
    try:
        #url = 'https://www.allrecipes.com/recipe/342043/'
        driver.get(url)
        scraper = scrape_me(url, wild_mode=True)
        title = scraper.title()
        if title == 'Johnsonville® Three Cheese Italian Style Chicken Sausage Skillet Pizza':
            continue
        title = title.replace('/', '_')
        title = title.replace('"',' ')

    except:
        print(count)
        continue
    try:
        close_popup = driver.find_element(By.CLASS_NAME, 'bx-close-x-adaptive-1')
        close_popup.click()
    except:
        close_popup = "None"

    #url = 'https://www.allrecipes.com/recipe/22341'

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


    while(3):
        try:
            load_more = driver.find_element(By.CLASS_NAME,'feedback__loadMoreButton')
            load_more.click()
            driver.implicitly_wait(2)
        except:
            break


    commands = []
    reviews = []
    try:
        commend_section = driver.find_element(By.CLASS_NAME, 'feedback__bodyContainer')
        commands = commend_section.find_elements(By.CLASS_NAME, 'feedback__reviewBody')
        for c in commands:
            body = c.text
            reviews.append(body)

    except:
        reviews = []



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

    food_object = json.dumps(foodData, indent=4)
    with open("/Users/cchen/Desktop/university/computerScience/631/ScrapedData/{0}_{1}.json".format(title, id),
              "w") as outfile:
        outfile.write(food_object)
    if count == 100:
        driver.implicitly_wait(10)
        count = 0

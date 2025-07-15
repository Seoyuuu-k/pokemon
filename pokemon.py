# day11
# py파일, 숫자t시작X,띄어쓰기X

import selenium.webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import csv
import os

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service
service = Service(executable_path="/usr/bin/chromedriver")

options = Options()
options.add_argument("--headless") # 추가하고 싶은 옵션 추가# 창없
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


url ="https://pokemonkorea.co.kr/pokedex"
driver = wb.Chrome(service=service, options=options)
driver.maximize_window()
driver.get(url)

# 포켓몬 선택
img = driver.find_element(By.CSS_SELECTOR, "img.img-fluid")
img.click()
time.sleep(1)

# 이상해씨 이름 
h3 = driver.find_element(By.TAG_NAME, "h3")
name = h3.text.split("\n")[1]


driver.close()


#csv
pokemon_exist = os.path.exists("pokemon.csv")
header = ["No","name"]

with open("pokemon.csv" , "a", newline="") as file:
    writer = csv.writer(file)

    if not pokemon_exist:
        writer.writerow(header)

    writer.writerow(["0001",name])
    print("포켓몬 저장완료")

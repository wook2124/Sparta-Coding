from bs4 import BeautifulSoup
from selenium import webdriver
import time
import dload

driver = webdriver.Chrome('chromedriver')
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%EB%B0%95%EB%B3%B4%EC%98%81")
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

i = 1
thumbnails = soup.select('#imgList > div > a > img')
for thumbnail in thumbnails:
    img = thumbnail['src']
    dload.save(img, f'1일차/img/{i}.png')
    i += 1

driver.quit()
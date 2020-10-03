from bs4 import BeautifulSoup
from selenium import webdriver
import time
import dload

driver = webdriver.Chrome('chromedriver')
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%ED%95%80%EA%B3%BC+%EC%A0%9C%EC%9D%B4%ED%81%AC")
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

i = 1
adventures = soup.select('#imgList > div > a > img')
for adventure in adventures:
    img = adventure['src']
    dload.save(img, f'imgs_homework/{i}.png')
    i += 1

driver.quit()
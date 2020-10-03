from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

from openpyxl import Workbook

url = "https://search.naver.com/search.naver?&where=news&query=%ED%95%9C%ED%99%94%EC%86%94%EB%A3%A8%EC%85%98&sm=tab_tmr&frm=mr&nso=so:r,p:all,a:all&sort=0"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

articles = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul > li')

wb = Workbook()
ws1 = wb.active
ws1.title = "한화솔루션 기사"

for article in articles:
    title = article.select_one('dl > dt > a').text
    link = article.select_one('dl > dt > a')['href']
    company = article.select_one('span._sp_each_source').text
    ws1.append([title, link, company])

driver.quit()
wb.save(filename='한화솔루션 기사.xlsx')
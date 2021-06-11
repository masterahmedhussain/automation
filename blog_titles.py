# To get the blog title from the ahmedhussaindev.com website 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get("https://ahmedhussaindev.com")

print("Title of the site:" + browser.title)


try:
    content = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "content"))
    )
    articles = content.find_elements_by_tag_name("article")
    print(articles)
    for article in articles:
        heading = article.find_elements_by_class_name("entry-title")
        print("Title of the Blog: " + heading[0].text)
finally:
    browser.quit()


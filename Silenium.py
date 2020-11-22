from time import sleep
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


username = 'Solodukha'
DRIVER_PATH = '/usr/bin/geckodriver'
GOOGLE_URL ='https://google.com'

driver = webdriver.Firefox(executable_path=DRIVER_PATH)
driver.get(GOOGLE_URL)
sleep(3)
found_element = driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input')
found_element.send_keys(f'twitter {username}')
found_element.send_keys(Keys.ENTER)
# This one does not work:
# twitter_page = driver.find_element_by_xpath(
#     '//h1[contains(text(), "Search Results")]/following-sibling::div/div/div/div/a').get_attribute('href')
sleep(3)
# driver.get(twitter_page)
driver.get('https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjx9o3_upbtAhWcAWMBHayZCosQFjAAegQIBxAC&url=https%3A%2F%2Ftwitter.com%2Fsolodukha%3Flang%3Den&usg=AOvVaw1KZRbLMvaZOp0B6wQEi4JQ')
follow = driver.find_element_by_xpath(
    '/a[contains(text(),"32")]'
)
follow.click()
# twitter_element = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div[2]/div[4]/div[2]/a/span[1]/span')
# print(twitter_element)
driver.close()
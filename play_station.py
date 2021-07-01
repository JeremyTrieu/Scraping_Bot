#find the right product
#if the product is not available, wait until it is available
#add product to cart
#add payment method when checkout
# checkout cart

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
from random import randint, randrange
import time
import random

PATH = 'C:\Program Files (x86)\chromedriver.exe'

TARGET_URL = 'https://www.target.com/p/blue-lizard-sensitive-mineral-sunscreen-lotion-spf-50-5-fl-oz/-/A-80139625#lnk=sametab'
AMAZON_TEST_URL = 'https://www.amazon.com/dp/B07XJWHFSZ/ref=cm_sw_r_cp_api_glt_fabc_SC6RT2D8TQNDJQV7W1Y4?_encoding=UTF8&psc=1&fbclid=IwAR1Gq-aMPUcrlFrgKe2T9lyW_kmu85oYZDxzvkuyq7aM446PO9hnbRtORAk'
CONST_WAIT_TIME = 6
PRICE_LIMIT = 1000.00
MY_USERNAME = ['jeremytrieu1612@gmail.com', '', '', '']
MY_PASSWORD = 'whatever'

class jeremy_cool_as_fuck:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(PATH)
    def sign_in(self):
        driver = self.driver

        #username typein
        username_element = driver.find_element_by_xpath("//input[@name='email']")
        username_element.clear()
        username_element.send_keys(self.username)

        #pretend like a real user
        time.sleep(randint(int(CONST_WAIT_TIME / 2), CONST_WAIT_TIME))
        username_element.send_keys(Keys.RETURN)
        time.sleep(randint(int(CONST_WAIT_TIME / 2), CONST_WAIT_TIME)) 

        #password typein
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)

        time.sleep(randint(int(CONST_WAIT_TIME / 2), CONST_WAIT_TIME))
        password_element.send_keys(Keys.RETURN)
        time.sleep(randint(int(CONST_WAIT_TIME / 2), CONST_WAIT_TIME))

    def find_product(self):
        driver = self.driver
        driver.get(AMAZON_TEST_URL)
        time.sleep(randint(int(CONST_WAIT_TIME / 2), CONST_WAIT_TIME))

        isAvailable = self.isProductAvailable()
        if isAvailable == 'Current Available.':
            time.sleep(randint(int(CONST_WAIT_TIME / 2), CONST_WAIT_TIME))
            self.find_product()
        elif isAvailable <= PRICE_LIMIT:
            buy_now = driver.find_element_by_name('submit.buy-now')
            buy_now.click()
            time.sleep(randint(int(CONST_WAIT_TIME / 2), CONST_WAIT_TIME))
            self.sign_in()

            place_order = driver.find_element_by_name('placeYourOrder1')
            time.sleep(randint(int(CONST_WAIT_TIME / 2), CONST_WAIT_TIME))

            #real buying shit is this part!!!!
            place_order.click()
            time.sleep(randint(int(CONST_WAIT_TIME / 2), CONST_WAIT_TIME))
            #real buying shit is this part!!!!

        else:
            time.sleep(randint(int(CONST_WAIT_TIME / 2), CONST_WAIT_TIME))
            self.find_product()


    def isProductAvailable(self):
        driver = self.driver
        available = driver.find_element_by_class_name('a-color-price').text
        if available == 'Current unavailable.':
            print(f'[ALERT AVAILABLE CHECK] {available}')
        else:
            print(f'[ALERT PRICE CHECK] {available}')
            return float(available[1:]) # $111.. => get rid of '$'

    def close_browser(self):
        self.driver.close()

#run the program
if __name__ == '__main__':
    for i in range(len(MY_USERNAME)):
        jeremy_bot = jeremy_cool_as_fuck(username = MY_USERNAME[i], password = MY_PASSWORD)
  
        jeremy_bot.find_product()
        #jeremy_bot.close_browser()



